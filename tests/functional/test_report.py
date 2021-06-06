from stats.report import show_report


def test_report_pychanges_karmabot(karmabot_dir, capfd):
    show_report(karmabot_dir, extension_pattern=".py")
    actual = capfd.readouterr()[0].splitlines()
    expected = [
        "--------------------------------------------------",
        "< Git Repo Activity Report (Python files only) >",
        "> Repo: karmabot",
        "--------------------------------------------------",
        "",
        "* Repo inserts and deletes per day:",
        "",
        "2017-06-25                             | 157",
        "2017-06-27                             |   7",
        "2017-08-07                             | 310",
        "2017-10-27                             |  61",
        "2018-07-21                             |  83",
        "2018-07-22                             |   8",
        "2018-07-23                             |   3",
        "2018-07-31                             |   2",
        "2018-08-27                             |  18",
        "2018-09-05                             | 127",
        "2018-09-06                             | 394",
        "2018-09-07                             | 357",
        "2018-09-08                             |  75",
        "2018-09-09                             |  12",
        "2018-09-10                             |   3",
        "2018-09-11                             |   3",
        "2018-09-19                             |  84",
        "2018-09-20                             |  86",
        "2018-10-08                             |   1",
        "2019-03-07                             |   4",
        "2019-04-06                             |  12",
        "2019-10-03                             | 107",
        "2019-10-09                             |   7",
        "2019-10-31                             | 1359",
        "2019-11-01                             |  33",
        "2019-11-02                             |  81",
        "2019-11-04                             |  46",
        "2019-11-20                             | 529",
        "2019-12-10                             |  72",
        "2020-01-01                             | 238",
        "2020-01-02                             |  35",
        "2020-04-30                             |  14",
        "2020-05-15                             |  40",
        "2020-07-14                             | 195",
        "2020-08-11                             |   3",
        "2020-09-07                             |   1",
        "2020-09-08                             |  33",
        "2020-09-09                             | 148",
        "2020-10-01                             | 278",
        "2020-10-05                             | 830",
        "2020-12-22                             |  25",
        "",
        "* Number of commits per day and author:",
        "",
        "2017-06-25",
        "- bbelderbos                           |   6",
        "2017-06-27",
        "- bbelderbos                           |   1",
        "2017-08-07",
        "- bbelderbos                           |   7",
        "2017-10-27",
        "- bbelderbos                           |   2",
        "2018-07-21",
        "- Bob Belderbos                        |   6",
        "2018-07-22",
        "- Bob Belderbos                        |   2",
        "2018-07-23",
        "- Bob Belderbos                        |   2",
        "2018-07-31",
        "- Bob Belderbos                        |   1",
        "2018-08-27",
        "- Bob Belderbos                        |   1",
        "2018-09-05",
        "- Bob Belderbos                        |   8",
        "2018-09-06",
        "- Bob Belderbos                        |  18",
        "2018-09-07",
        "- Bob Belderbos                        |  22",
        "2018-09-08",
        "- Bob Belderbos                        |   3",
        "- PyBites                              |   1",
        "- pybites                              |   1",
        "2018-09-09",
        "- Bob Belderbos                        |   1",
        "2018-09-10",
        "- Bob Belderbos                        |   1",
        "2018-09-11",
        "- Bob Belderbos                        |   1",
        "2018-09-19",
        "- jnyjny                               |   1",
        "2018-09-20",
        "- Bob Belderbos                        |   2",
        "2018-10-08",
        "- Mayank Singh                         |   1",
        "2019-03-07",
        "- Bob Belderbos                        |   1",
        "2019-04-06",
        "- Bob Belderbos                        |   3",
        "2019-10-03",
        "- pmayd                                |   3",
        "2019-10-09",
        "- pmayd                                |   1",
        "2019-10-31",
        "- Bob Belderbos                        |   4",
        "- Patrick-Oliver Groß                  |   1",
        "2019-11-01",
        "- Bob Belderbos                        |   1",
        "2019-11-02",
        "- Bob Belderbos                        |   2",
        "2019-11-04",
        "- Bob Belderbos                        |   2",
        "- Patrick-Oliver Groß                  |   2",
        "2019-11-20",
        "- Bob Belderbos                        |   5",
        "- Patrick-Oliver Groß                  |   3",
        "2019-12-10",
        "- AJ Kerrigan                          |   1",
        "2020-01-01",
        "- AJ Kerrigan                          |   1",
        "2020-01-02",
        "- AJ Kerrigan                          |   1",
        "- Bob Belderbos                        |   1",
        "2020-04-30",
        "- Patrick-Oliver Groß                  |   1",
        "2020-05-15",
        "- Patrick-Oliver Groß                  |   1",
        "2020-07-14",
        "- Patrick-Oliver Groß                  |   1",
        "2020-08-11",
        "- Patrick-Oliver Groß                  |   1",
        "2020-09-07",
        "- AJ Kerrigan                          |   1",
        "2020-09-08",
        "- Michael Aydinbas                     |   1",
        "2020-09-09",
        "- Bob Belderbos                        |   1",
        "- Michael Aydinbas                     |   1",
        "2020-10-01",
        "- Michael Aydinbas                     |   1",
        "2020-10-05",
        "- Ivan Gonzalez                        |   1",
        "2020-12-22",
        "- Patrick-Oliver Groß                  |   1",
        "",
        "* Files that are most often found in commits:",
        "",
        "bot/slack.py                           |  73",
        "bot/karma.py                           |  19",
        "commands/topchannels.py                |  15",
        "tests/test_bot.py                      |  13",
        "bot/__init__.py                        |  10",
        "commands/welcome.py                    |  10",
        "test/tests.py                          |  10",
        "commands/score.py                      |   6",
        "tests/slack_testdata.py                |   5",
        "utils/get_botid.py                     |   5",
        "--------------------------------------------------",
    ]
    assert actual == expected


def test_report_allchanges_karmabot(karmabot_dir, capfd):
    show_report(karmabot_dir)
    actual = capfd.readouterr()[0].splitlines()
    expected = [
        "--------------------------------------------------",
        "< Git Repo Activity Report (Python files only) >",
        "> Repo: karmabot",
        "--------------------------------------------------",
        "",
        "* Repo inserts and deletes per day:",
        "",
        "2017-06-25                             | 248",
        "2017-06-26                             |  11",
        "2017-06-27                             |   7",
        "2017-08-07                             | 482",
        "2017-10-03                             |   4",
        "2017-10-27                             | 119",
        "2017-10-28                             |  34",
        "2018-07-21                             | 201",
        "2018-07-22                             |   8",
        "2018-07-23                             |   3",
        "2018-07-31                             |   2",
        "2018-08-27                             |  18",
        "2018-09-05                             | 131",
        "2018-09-06                             | 397",
        "2018-09-07                             | 357",
        "2018-09-08                             | 131",
        "2018-09-09                             |  12",
        "2018-09-10                             |   5",
        "2018-09-11                             |   3",
        "2018-09-19                             |  84",
        "2018-09-20                             | 172",
        "2018-10-08                             |   1",
        "2018-10-09                             |   1",
        "2018-11-01                             |   4",
        "2019-03-07                             |   6",
        "2019-04-06                             |  12",
        "2019-04-24                             |   2",
        "2019-07-02                             |  10",
        "2019-10-03                             | 178",
        "2019-10-09                             | 156",
        "2019-10-31                             | 1585",
        "2019-11-01                             |  40",
        "2019-11-02                             | 388",
        "2019-11-04                             |  88",
        "2019-11-07                             |  34",
        "2019-11-20                             | 631",
        "2019-12-10                             |  75",
        "2020-01-01                             | 238",
        "2020-01-02                             |  36",
        "2020-04-30                             |  14",
        "2020-05-15                             |  41",
        "2020-07-06                             |   2",
        "2020-07-14                             | 2177",
        "2020-08-11                             | 264",
        "2020-08-12                             |   6",
        "2020-09-04                             |   2",
        "2020-09-07                             |   9",
        "2020-09-08                             | 120",
        "2020-09-09                             | 416",
        "2020-10-01                             | 1029",
        "2020-10-05                             | 849",
        "2020-12-22                             | 555",
        "2021-03-23                             | 557",
        "2021-05-31                             |  12",
        "",
        "* Number of commits per day and author:",
        "",
        "2017-06-25",
        "- bbelderbos                           |   9",
        "2017-06-26",
        "- bbelderbos                           |   3",
        "2017-06-27",
        "- bbelderbos                           |   1",
        "2017-08-07",
        "- bbelderbos                           |  17",
        "2017-10-03",
        "- bbelderbos                           |   2",
        "2017-10-27",
        "- bbelderbos                           |   4",
        "- PyBites                              |   1",
        "2017-10-28",
        "- PyBites                              |   1",
        "2018-07-21",
        "- Bob Belderbos                        |   7",
        "2018-07-22",
        "- Bob Belderbos                        |   2",
        "2018-07-23",
        "- Bob Belderbos                        |   2",
        "2018-07-31",
        "- Bob Belderbos                        |   1",
        "2018-08-27",
        "- Bob Belderbos                        |   1",
        "2018-09-05",
        "- Bob Belderbos                        |   9",
        "2018-09-06",
        "- Bob Belderbos                        |  20",
        "2018-09-07",
        "- Bob Belderbos                        |  22",
        "2018-09-08",
        "- Bob Belderbos                        |   4",
        "- PyBites                              |   2",
        "- pybites                              |   1",
        "2018-09-09",
        "- Bob Belderbos                        |   1",
        "2018-09-10",
        "- Bob Belderbos                        |   2",
        "2018-09-11",
        "- Bob Belderbos                        |   1",
        "2018-09-19",
        "- jnyjny                               |   1",
        "2018-09-20",
        "- Bob Belderbos                        |   3",
        "2018-10-08",
        "- Mayank Singh                         |   1",
        "2018-10-09",
        "- Bob Belderbos                        |   1",
        "2018-11-01",
        "- PyBites                              |   2",
        "2019-03-07",
        "- Bob Belderbos                        |   2",
        "2019-04-06",
        "- Bob Belderbos                        |   3",
        "2019-04-24",
        "- PyBites                              |   1",
        "2019-07-02",
        "- Bob Belderbos                        |   2",
        "2019-10-03",
        "- pmayd                                |   3",
        "2019-10-09",
        "- Michael Aydinbas                     |   1",
        "- pmayd                                |   2",
        "2019-10-31",
        "- Bob Belderbos                        |  11",
        "- Patrick-Oliver Groß                  |   1",
        "2019-11-01",
        "- Bob Belderbos                        |   4",
        "2019-11-02",
        "- Bob Belderbos                        |   3",
        "2019-11-04",
        "- Bob Belderbos                        |   2",
        "- PyBites                              |   1",
        "- Patrick-Oliver Groß                  |   2",
        "2019-11-07",
        "- Bob Belderbos                        |   1",
        "2019-11-20",
        "- Bob Belderbos                        |  14",
        "- Patrick-Oliver Groß                  |   3",
        "2019-12-10",
        "- Patrick-Oliver Groß                  |   1",
        "- AJ Kerrigan                          |   1",
        "2020-01-01",
        "- AJ Kerrigan                          |   1",
        "2020-01-02",
        "- AJ Kerrigan                          |   1",
        "- Bob Belderbos                        |   1",
        "2020-04-30",
        "- Patrick-Oliver Groß                  |   1",
        "2020-05-15",
        "- Patrick-Oliver Groß                  |   1",
        "2020-07-06",
        "- Bob Belderbos                        |   1",
        "2020-07-14",
        "- Bob Belderbos                        |   1",
        "- Patrick-Oliver Groß                  |   1",
        "2020-08-11",
        "- Bob Belderbos                        |   1",
        "- Patrick-Oliver Groß                  |   1",
        "2020-08-12",
        "- Bob Belderbos                        |   2",
        "2020-09-04",
        "- Bob Belderbos                        |   1",
        "2020-09-07",
        "- AJ Kerrigan                          |   2",
        "2020-09-08",
        "- Bob Belderbos                        |   1",
        "- Patrick-Oliver Groß                  |   2",
        "- Michael Aydinbas                     |   1",
        "2020-09-09",
        "- Patrick-Oliver Groß                  |   2",
        "- Bob Belderbos                        |   4",
        "- Michael Aydinbas                     |   2",
        "2020-10-01",
        "- Patrick-Oliver Groß                  |   2",
        "- Michael Aydinbas                     |   2",
        "2020-10-05",
        "- Michael Aydinbas                     |   1",
        "- Ivan Gonzalez                        |   1",
        "2020-12-22",
        "- Bob Belderbos                        |   1",
        "- Patrick-Oliver Groß                  |   1",
        "2021-03-23",
        "- Patrick-Oliver Groß                  |   1",
        "2021-05-31",
        "- pre-commit-ci[bot]                   |   1",
        "",
        "* Files that are most often found in commits:",
        "",
        "bot/slack.py                           |  77",
        "README.md                              |  28",
        "bot/karma.py                           |  21",
        "commands/topchannels.py                |  17",
        "tests/test_bot.py                      |  14",
        "main.py                                |  14",
        ".gitignore                             |  13",
        "pyproject.toml                         |  12",
        "test/tests.py                          |  12",
        "requirements.txt                       |  11",
        "--------------------------------------------------",
    ]
    assert actual == expected
