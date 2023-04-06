from setuptools import setup


setup(
		name				= "jandi",
		version			 = "0.0.1",
		description		 = "Jandi webhook Library for Python3",
		url				 = "https://github.com/taeng42/ft_apy.git",
		author			  = "Hyundong",
		author_email		= "hyundong@42seoul.kr",
		license			 = "mit",
		#packages			= find_packages(exclude = []),
		install_requires	= ["setuptools", "wheel", "urllib3"],
		packages			= ["jandi"],
		zip_safe			= False,
		python_requires	 = '>=3',
		classifiers		 = [
			'Programming Language :: Python :: 3.6',
			'Programming Language :: Python :: 3.7',
			'Programming Language :: Python :: 3.8',
			'Programming Language :: Python :: 3.9',
			'Programming Language :: Python :: 3.10',
			'Programming Language :: Python :: 3.11',
			],
		)
