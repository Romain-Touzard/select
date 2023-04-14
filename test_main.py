import unittest
from unittest.mock import patch
from main import add_to_notion

class TestClipboardHistory(unittest.TestCase):

    @patch('main.notion.pages.create')
    def test_add_to_notion(self, mock_create):
        title = "Test Title"
        content = "Test Content"

        add_to_notion(title, content)

        mock_create.assert_called_once()
        args, kwargs = mock_create.call_args
        self.assertIn(title, kwargs['properties']['Titre']['title'][0]['text']['content'])
        self.assertIn(content, kwargs['properties']['Contenu']['rich_text'][0]['text']['content'])

if __name__ == '__main__':
    unittest.main()
