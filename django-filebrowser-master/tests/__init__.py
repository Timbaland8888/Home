import os
import shutil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from filebrowser.settings import DIRECTORY, VERSIONS_BASEDIR
from filebrowser.base import FileObject
from filebrowser.sites import site


class FilebrowserTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(FilebrowserTestCase, cls).setUpClass()
        User = get_user_model()
        cls.user = User.objects.create_user('testuser', 'test@domain.com', 'password')
        cls.user.is_staff = True
        cls.user.save()

    def setUp(self):
        self.DIRECTORY = DIRECTORY
        self.TEST_PATH = os.path.join(site.storage.location, '_test').replace('\\','/')
        self.DIRECTORY_PATH = os.path.join(site.storage.location, DIRECTORY).replace('\\','/')
        self.VERSIONS_PATH = os.path.join(site.storage.location, VERSIONS_BASEDIR).replace('\\','/')
        # print self.TEST_PATH+'3333333333'
        # if os.path.exists(self.TEST_PATH):
        #     raise Exception('TEST_PATH Already Exists')


        self.TEMP_PATH = os.path.join(self.TEST_PATH, 'tempfolder').replace('\\','/')
        self.FOLDER_PATH = os.path.join(self.DIRECTORY_PATH, 'folder').replace('\\','/')
        self.SUBFOLDER_PATH = os.path.join(self.FOLDER_PATH, 'subfolder').replace('\\','/')
        self.CREATEFOLDER_PATH = os.path.join(self.DIRECTORY_PATH, 'create').replace('\\','/')
        self.PLACEHOLDER_PATH = os.path.join(self.DIRECTORY_PATH, 'placeholders').replace('\\','/')
        print self.PLACEHOLDER_PATH

        self.STATIC_IMG_PATH = os.path.join(settings.BASE_DIR, 'filebrowser', "static", "filebrowser", "img", "testimage.jpg").replace('\\','/')

        self.STATIC_IMG_BAD_NAME_PATH = os.path.join(settings.BASE_DIR, 'filebrowser', "static", "filebrowser", "img", "TEST_IMAGE_000.jpg").replace('\\','/')

        self.F_IMAGE = FileObject(os.path.join(DIRECTORY, 'folder', "testimage.jpg").replace('\\','/'), site=site)
        self.F_MISSING = FileObject(os.path.join(DIRECTORY, 'folder', "missing.jpg").replace('\\','/'), site=site)
        self.F_FOLDER = FileObject(os.path.join(DIRECTORY, 'folder').replace('\\','/'), site=site)
        self.F_SUBFOLDER = FileObject(os.path.join(DIRECTORY, 'folder', 'subfolder').replace('\\','/'), site=site)
        self.F_CREATEFOLDER = FileObject(os.path.join(DIRECTORY, 'create').replace('\\','/'), site=site)
        self.F_TEMPFOLDER = FileObject(os.path.join('_test', 'tempfolder').replace('\\','/'), site=site)

        os.makedirs(self.FOLDER_PATH)
        os.makedirs(self.SUBFOLDER_PATH)

    def tearDown(self):
        shutil.rmtree(self.TEST_PATH)
