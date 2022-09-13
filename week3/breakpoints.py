import pandas as pd

#  Create a DataFrame from a dictionary of lists
population = [38332521, 26448193, 19651127, 19552860, 12882135]
area = [423967, 170312, 149995, 141297, 695662]
state_names = ['California','Florida','Illinois','New York','Texas']

def create_df(state_names,population,area):
    states_df = pd.DataFrame({'Population':population},index=state_names) # Index specifies row names
    breakpoint()
    states_df['Area'] = area
    breakpoint()
    return states_df

states_df = create_df(state_names,population,area)
print(states_df.head())

# Run with debugging: python breakpoints.py
# Run without debugging: PYTHONBREAKPOINT=0 python breakpoints.py