import unittest
from github_api import GitHubAPI
unittest.TestLoader.sortTestMethodsUsing = None

class TestGitHubAPI(unittest.TestCase):
    
    gh = GitHubAPI("Liam-Brew")
    repos = gh.get_repos()
    commits = gh.get_commits()
    run = gh.run()

    def test_get_repos_quantity(self):
        self.assertEqual(len(repos), 8, "There should be 8 repos present")
    
    def test_get_repos_names(self):
        self.assertEqual(repos, ['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567'], ['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567'])

    def test_specific_get_commits(self):
        self.assertEqual(commits['CS-135'], 6, 'Repo CS-135 should have 6 commits')

    def test_run_status_ok(self):
        self.assertEqual(run, 200, "Run status should be ok")

    def test_404_repo(self):
        gh1 = GitHubAPI("adwdawwadwwdadwadwwdawadwadddddddddddddddddddd")
        self.assertEqual(gh1.run(), 404, "This user is not on GitHub")
        
if __name__ == "__main__":
    unittest.main()
