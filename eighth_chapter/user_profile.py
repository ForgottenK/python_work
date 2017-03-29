def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = first
	for k, v in user_info.items():
		profile[k] = v
	return profile

user_profile = build_profile('frank', 'king', location='beijing', job='coding')
print(user_profile)