import unittest
from unittest.mock import patch
from action import delete_old_ecr_images

class TestDeleteOldEcrImages(unittest.TestCase):

    @patch('action.boto3.client')
    def test_delete_old_ecr_images(self, boto3_client_mock):
        # Mock the paginator
        paginator_mock = boto3_client_mock.return_value.get_paginator.return_value
        paginator_mock.paginate.return_value = [{'imageDetails': []}]

        # Test the function with some parameters
        repository_name = 'test-repo'
        num_to_keep = 10
        dry_run = False
        delete_untagged_images = False

        deleted_count = delete_old_ecr_images(repository_name, num_to_keep, dry_run, delete_untagged_images)

        # Asserts
        self.assertEqual(deleted_count, 0)  # No images to delete
        self.assertFalse(boto3_client_mock.return_value.batch_delete_image.called)  # Ensure batch_delete_image wasn't called

if __name__ == '__main__':
    unittest.main()