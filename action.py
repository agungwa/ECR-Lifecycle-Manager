import boto3
import sys

def delete_old_ecr_images(repository_name, num_to_keep=10, dry_run=True, delete_untagged_images=False):
    if len(sys.argv) < 2 or sys.argv[1] == "discover":
        # Handle the case where 'discover' is passed or there are insufficient arguments
        # You can set default values or handle the error accordingly
        print("Continuing without repository_name, num_to_keep, dry_run, and delete_untagged_images.")
    else:
        try:
            repository_name = sys.argv[1]
            num_to_keep = int(sys.argv[2])
            dry_run = sys.argv[3].lower() == 'true'
            delete_untagged_images = sys.argv[4].lower() == 'true'
        except IndexError:
            # Handle the case where IndexError occurs due to insufficient arguments
            print("Insufficient arguments provided.")
            return
    print({'repository_name':repository_name, 'num_to_keep':num_to_keep, 'dry_run':dry_run, 'delete_untagged_images':delete_untagged_images})
    # return True
    ecr = boto3.client('ecr')
    # Counter for deleted images
    deleted_count = 0

    # Paginate through the list of images
    paginator = ecr.get_paginator('describe_images')
    for page in paginator.paginate(repositoryName=repository_name):
        # Sort images by pushing time
        images = sorted(page['imageDetails'], key=lambda x: x['imagePushedAt'])

        # Calculate how many images to delete
        num_to_delete = max(len(images) - num_to_keep, 0)

        # Delete old images or just print them for dry run
        for image in images[:num_to_delete]:
            image_digest = image['imageDigest']

            # Check if the image is untagged and delete it if delete_untagged_images is True
            if 'imageTags' not in image and delete_untagged_images:
                if not dry_run:
                    ecr.batch_delete_image(
                        repositoryName=repository_name,
                        imageIds=[
                            {
                                'imageDigest': image_digest
                            }
                        ]
                    )
                deleted_count += 1
                print(f"{'Would delete' if dry_run else 'Deleted'} untagged image with digest: {image_digest}")
            
            # Check if the image is tagged and delete it if delete_untagged_images is False
            elif 'imageTags' in image and not delete_untagged_images:
                if not dry_run:
                    ecr.batch_delete_image(
                        repositoryName=repository_name,
                        imageIds=[
                            {
                                'imageDigest': image_digest
                            }
                        ]
                    )
                deleted_count += 1
                print(f"{'Would delete' if dry_run else 'Deleted'} tagged image with digest: {image_digest}")
    print(f"Total untagged images that would be deleted in dry run: {deleted_count}")
    return deleted_count

# Replace 'your-repository-name' with your actual ECR repository name
# Set num_to_delete_limit=None to delete all the images that should be deleted based on num_to_keep
# Set num_to_delete_limit to a specific number if you want to limit the deletion to a certain number of oldest images
# Set delete_untagged_images=True to delete only the untagged images
# Set delete_untagged_images=False to delete only the tagged images
# Accessing user inputs

if __name__ == "__main__":
    
    deleted_count = delete_old_ecr_images('', 10, True, True)
    print(f"Total images deleted: {deleted_count}")
