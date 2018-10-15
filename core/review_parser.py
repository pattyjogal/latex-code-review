import os

class ReviewParser:
    accepted_extensions = set()
    directory_name = ""
    files_to_read = []
    parsed_output = {}
    start_delim = "//>"
    end_delim = "//<"

    def __init__(self, accepted_extensions, directory_name=None, github_url=None):
        """
        Constructs the Review Parser with the given specifications
        Note that one and only one of directory_name or github_url must be set.
        :param: accepted_extensions     A list of filetype extensions that we will look out for
                                        in the traversal
        :param: directory_name          An optional parameter that is the path to a repo previously
                                        cloned to the local machine
        :param: github_url              A url to the GitHub repository (does not need to be perfect:
                                        can be formatted as user/repo, http://github.com/user/repo.git, etc)
        """
        self.accepted_extensions = set(accepted_extensions)

        if directory_name is not None:
            self.directory_name = directory_name
        elif github_url is not None:
            # TODO: Clone down the GH repo into a local dir, and set directory_name
            pass
        else:
            raise AssertionError("Constructor of ReviewParser requires directory_name or github_url to be set.")

    def parse_repository(self):
        """
        Takes a github repository, identifies code surrounded by the defined delimiters, and parses it into JSON.
        """
        
        # Walk through the repository directory, looking for files with the correct extension type
        for subdir, dirs, files in os.walk(self.directory_name):
            for f in files:
                filepath = subdir + os.sep + f
                if f.split('.')[-1] in self.accepted_extensions:
                    self.files_to_read.append(f)

        print(self.files_to_read)

