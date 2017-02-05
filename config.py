class accesstoken():
	def assign_token(self):
		token="EwD4Aq1DBAAUGCCXc8wU/zFu9QnLdZXy+YnElFkAAW+5cac5VvNkreW5Pd8CZgMcVdC3fbNEFdHbcL6qEX+VD54doKQvP29V2Zw+PmG42/g9SaizMPwt8GFU06khPQu8FBLqs5kzaVLOE5pMW2FPaiN146kvAQPXqyVpIuxq9uG96Bcm0coR1VVX1OHV4rVnGElv8uWImrkFNGQGIel9avoM9zX1/lgaSBZUazqDxjY1RQDOFLqA/PoK0BJRt+7/gcsYQP19e/cNQReqNmwr7Lgqwhro0Z8EhBWkLNYuiR14L3qGWhGiBfXpYO1kiSPVhGtxrtYYutZOTf74tXCK+bm1bvpECKUuVRofL0RsWYIQf65r6qiVn2OTxdApCEYDZgAACGzpGeAwE2DhyAGXig4hbe3fDWJ0yReiZGoi3L93f/AH9+ewzA7FH80poolKGbsawHWZmxRtwFb3zi64d81jwRcze1zs2r9bT7RWwLrD8OLWsvBROuC7iojagM8riZtYY7+8ZUHGDOoA2XRKcebZCCU5LBQMNSXfDdFeBh0iTtX9qO1HaI0JiIdRAE2SdCU4P+PiyBlv78QTVFbCczRrlO08D9kzpSQ/hZfCTtucZDl7BjsGpvsFQPkAVqTNsf2RWiJfNB1YuGHUBiHa44ngAZnqKQJi/e33JEtMcWUgcFPfK4hJhaUoUAd4lx8o9cWdXtvHXH035VXn1DE/VRDnnImZC/i7xssINeiTWI8BSrsEZ3b0ZHC3k3U0raItzdUU6aTQZmWw8KX1+WYWRJiUf1tx5qerMHMy1398l9tDUhTfSbHmBqZD1J+ufZtlgiV7ciY7YlKfn5cBQBbEeNnFAWFG1jJ8+s4ugUgxxl1IrBhqAuZ46D98E2Qi7Bf/PfI5mrUj8huiFrCHdxpvbdm0K24JtjUdRIR8c+6DW7sKXneyL7cpzKrc17HLyakBWzINxVwUayqCwqBlNM0OMVIcY59+ulNmTma9FHjFLiXPdNZJsZv9AQ=="
		return token

class dbconnect():
	def db_config(self):
		db = {
	    	'host':'localhost',
	    	'database':'codefundoapp',
	    	'user':'root',
	    	'password':'deepak'
		}		
		return db