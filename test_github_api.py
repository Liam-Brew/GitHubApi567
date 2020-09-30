import unittest
from github_api import GitHubAPI

class TestGitHubAPI(unittest.TestCase):

    def test_get_repos_quantity(self):
        gh = GitHubAPI("Liam-Brew")
        self.assertEqual(len(gh.get_repos()), 8, "There should be 8 repos present")
    
    def test_get_repos_names(self):
        gh = GitHubAPI("Liam-Brew")
        self.assertEqual(gh.get_repos(), "['CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567']", 'CS-135', 'CS-284', 'GitHubApi567', 'SSW-215', 'SSW-322', 'SSW-345', 'SSW-567', 'Triangle567')

    def test_specific_get_commits(self):
        gh = GitHubAPI("Liam-Brew")
        commits = gh.get_commits()
        self.assertEqual(commits['CS-135'], 6, 'Repo CS-135 should have 6 commits')

    def test_run_status_ok(self):
        gh = GitHubAPI("Liam-Brew")
        self.assertEqual(gh.run(), 200, "Run status should be ok")

    def test_404_repo(self):
        gh = GitHubAPI("adwdawwadwwdadwadwwdawadwadddddddddddddddddddd")
        self.assertEqual(gh.run(), 404, "This user is not on GitHub")

    def test_403(self):
        gh = GitHubAPI("Liam-Brew")
        for i in range(10):
            gh.run()
        self.assertEqual(gh.run(), 403, "Too many requests have been performed")

if __name__ == "__main__":
    unittest.main()
