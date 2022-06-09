```
conda activate py39
conda install pytest-cov
conda update -n base -c defaults conda

pytest -vv --cov=python python/tests/sample_test/* --log-cli-level=DEBUG --cov-report=html > log.txt

pytest -vv python/tests/sample_test/test_*.py > log.txt

```