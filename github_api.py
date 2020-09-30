import requests
import json

class GitHubAPI:
    
    def __init__(self, id):
        self.id = id      
        self.repo_status = 0
        self.commit_status = 0

        self.repos = []
        self.commits = {}

    def get_repos(self):
        try:
            r = requests.get(f'https://api.github.com/users/{self.id}/repos')
            self.repo_status = r.status_code
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return
        for repo in r.json():
            self.repos.append(repo["name"])
        return self.repos

    def get_commits(self):
        for repo in self.repos:
            try:
                r = requests.get(f'https://api.github.com/repos/{self.id}/{repo}/commits')
                self.commit_status = r.status_code
                r.raise_for_status()
            except requests.exceptions.HTTPError as error:
                return
            self.commits[repo] = len(r.json())
        return self.commits

    def print_data(self):
        for repo in self.repos:
            print(f'Repo: {repo} Number of commits: {self.commits[repo]}')

    def run(self):
        self.get_repos()
        if self.repo_status != 200:
            print(f'{self.repo_status} Error getting repos')
            return self.repo_status

        self.get_commits()
        if self.commit_status != 200:
            print(f'{self.commit_status} Error getting commits')
            return self.repo_status

        self.print_data()
        return 200

if __name__ == "__main__":
    githubapi = GitHubAPI("Liam-Brew")
    githubapi.run()