{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import unittest\n",
    "\n",
    "from Gaussiandistribution import Gaussian\n",
    "\n",
    "\n",
    "class TestGaussianClass(unittest.TestCase):\n",
    "    def setUp(self):\n",
    "        self.gaussian = Gaussian(25, 2)\n",
    "\n",
    "    def test_initialization(self): \n",
    "        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')\n",
    "        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')\n",
    "\n",
    "    def test_pdf(self):\n",
    "        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\\\n",
    "         'pdf function does not give expected result') \n",
    "\n",
    "    def test_meancalculation(self):\n",
    "        self.gaussian.read_data_file('numbers.txt', True)\n",
    "        self.assertEqual(self.gaussian.calculate_mean(),\\\n",
    "         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')\n",
    "\n",
    "    def test_stdevcalculation(self):\n",
    "        self.gaussian.read_data_file('numbers.txt', True)\n",
    "        self.assertEqual(round(self.gaussian.stdev, 2), 92.87, 'sample standard deviation incorrect')\n",
    "        self.gaussian.read_data_file('numbers.txt', False)\n",
    "        self.assertEqual(round(self.gaussian.stdev, 2), 88.55, 'population standard deviation incorrect')\n",
    "                \n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
