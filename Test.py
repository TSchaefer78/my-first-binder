from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
df
