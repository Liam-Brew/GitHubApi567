import unittest
from unittest.mock import patch, Mock
from github_api import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    
    @patch.object(GitHubAPI, 'get_repos')
    def test_get_repos_quantity(self, mock_method):
        repo_data = ['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567']
        mock_method.return_value = repo_data

        repos = GitHubAPI("Liam-Brew").get_repos()

        self.assertEqual(len(repos), 8, "There should be 8 repos present")
    
    @patch.object(GitHubAPI, 'get_repos')
    def test_get_repos_names(self, mock_method):
        repo_data = ['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567']

        mock_method.return_value = repo_data

        repos = GitHubAPI("Liam-Brew").get_repos()

        self.assertEqual(repos, ['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567'], ['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567'])

    @patch.object(GitHubAPI, 'get_commits')
    def test_specific_get_commits(self, mock_method):
        commit_data = {'CS-135': 6, 'CS-284': 30, 'GitHubApi567': 13, 'SSW-215': 11, 'SSW-322': 29, 'SSW-345': 30, 'SSW-567': 30, 'Triangle567': 6}

        mock_method.return_value = commit_data

        print(mock_method.return_value)

        commits = GitHubAPI("Liam-Brew").get_commits()

        self.assertEqual(commits['CS-135'], 6, 'Repo CS-135 should have 6 commits')

    @patch('github_api.requests.get')
    def test_run_status_ok(self, mock_get):
        mock_get.return_value.status_code = 200
        gh = GitHubAPI("Liam-Brew")
        self.assertEqual(gh.run(), 200, "Run status should be ok")

    @patch('github_api.requests.get')
    def test_nonexistant_user(self, mock_get):
        mock_get.return_value.status_code = 404
        gh1 = GitHubAPI("adwdawwadwwdadwadwwdawadwadddddddddddddddddddd")
        self.assertEqual(gh1.run(), 404, "This user is not on GitHub")
        
if __name__ == "__main__":
    unittest.main()
