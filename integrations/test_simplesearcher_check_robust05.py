#
# Pyserini: Python interface to the Anserini IR toolkit built on Lucene
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import unittest

from integrations.simplesearcher_checker import SimpleSearcherChecker


class TestSearchIntegration(unittest.TestCase):
    def setUp(self):
        # The current directory depends on if you're running inside an IDE or from command line.
        curdir = os.getcwd()
        if curdir.endswith('integrations'):
            anserini_root = '../../anserini'
            pyserini_root = '..'
        else:
            anserini_root = '../anserini'
            pyserini_root = '.'

        self.checker = SimpleSearcherChecker(
            anserini_root=anserini_root,
            index=os.path.join(anserini_root, 'indexes/lucene-index.robust05.pos+docvectors+raw'),
            topics=os.path.join(pyserini_root, 'tools/topics-and-qrels/topics.robust05.txt'),
            pyserini_topics='robust05',
            qrels=os.path.join(pyserini_root, 'tools/topics-and-qrels/qrels.robust05.txt'))

    def test_bm25(self):
        self.assertTrue(self.checker.run('robust05_bm25', '-bm25', '--bm25'))

    def test_bm25_rm3(self):
        self.assertTrue(self.checker.run('robust05_bm25_rm3', '-bm25 -rm3', '--bm25 --rm3'))

    def test_qld(self):
        self.assertTrue(self.checker.run('robust05_qld', '-qld', '--qld'))

    def test_qld_rm3(self):
        self.assertTrue(self.checker.run('robust05_qld_rm3', '-qld -rm3', '--qld --rm3'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()