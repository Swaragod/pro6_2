import unittest
from parameterized import parameterized
from main import folder_info, create_folder

class YaFolderTest(unittest.TestCase):

    @parameterized.expand([
        ('SomeFolder1', 201), # Папка успешно создана
        ('SomeFolder1', 409) # Такая папка уже существует
    ])
    def test_create_folder(self, folder_name, result):
        self.assertEqual(create_folder(folder_name), result)

    @parameterized.expand([
        ('SomeFolder2', 404), # Папка не найдена( и не должна )
        ('SomeFolder1', 200) # Папка найдена
    ])
    def test_folder_info(self, folder_name, result):
        self.assertEqual(folder_info(folder_name), result)

