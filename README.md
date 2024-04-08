# Delete Old ECR Images GitHub Action

This GitHub Action helps you manage your Amazon ECR (Elastic Container Registry) repositories by deleting old images, optionally limiting deletion to untagged images. It allows you to specify parameters such as the repository name, the number of latest images to keep, whether to perform a dry run, and whether to delete only untagged images.

Usage
-----

yamlCopy code

`- name: Delete old ECR images
  uses: agungwa/ECR-Lifecycle-Manager@v1.0.0
  with:
    repo_name: <your-repository-name>
    num_to_keep: 10
    dry_run: true
    delete_untagged_images: false

Inputs
------

-   `repo_name`: (required) The name of the ECR repository to delete images from.
-   `num_to_keep`: (optional) The number of latest images to keep. Default is 10.
-   `dry_run`: (optional) Perform a dry run without actually deleting images. Default is true.
-   `delete_untagged_images`: (optional) Delete only untagged images. Default is false.

Example
-------

yamlCopy code

`- name: Delete old ECR images
  uses: agungwa/ECR-Lifecycle-Managers@v1.0.0
  with:
    repo_name: my-ecr-repo
    num_to_keep: 5
    dry_run: false
    delete_untagged_images: true`

License
-------

This project is licensed under the [MIT License](https://github.com/agungwa/ECR-Lifecycle-Managers/blob/master/LICENSE).

Feedback
--------

If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or pull request in the [GitHub repository](https://github.com/agungwa/ECR-Lifecycle-Managers).