import os
import numpy as np
import pickle
import pandas as pd

def convert_deap_dat_to_csv(input_folder, output_folder):
    """
    Converts all DEAP dataset .dat files into CSV format, preserving trial information,
    while dropping columns from Channel_33 to Channel_40.
    
    Parameters:
    input_folder (str): Path to the folder containing .dat files.
    output_folder (str): Path to save the converted CSV files.
    """
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all .dat files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".dat"):
            file_path = os.path.join(input_folder, filename)
            subject_id = filename.split('.')[0]  # Extract subject ID (e.g., 's01')
            
            # Load .dat file
            with open(file_path, 'rb') as file:
                data = pickle.load(file, encoding='latin1')
            
            # Extract EEG data and labels
            eeg_data = data['data']  # Shape (40, 40, 8064)
            labels = data['labels']  # Shape (40, 4)
            
            # Create a list to hold all trials
            all_trials = []
            
            # Process each trial
            for trial_idx in range(40):
                # Reshape data for this trial: (40, 8064) -> (8064, 40)
                trial_data = eeg_data[trial_idx].T  # Transpose to (8064, 40)
                
                # Create a DataFrame for this trial
                columns = [f'Channel_{c+1}' for c in range(40)]
                df_trial = pd.DataFrame(trial_data, columns=columns)
                
                # Drop Channel_33 to Channel_40
                df_trial = df_trial.drop(columns=[f'Channel_{c}' for c in range(33, 41)])
                
                # Add trial number and labels
                df_trial['Trial'] = trial_idx + 1
                df_trial['Valence'] = labels[trial_idx, 0]
                df_trial['Arousal'] = labels[trial_idx, 1]
                df_trial['Dominance'] = labels[trial_idx, 2]
                df_trial['Liking'] = labels[trial_idx, 3]
                
                # Append to the list
                all_trials.append(df_trial)
            
            # Combine all trials into a single DataFrame
            df = pd.concat(all_trials, ignore_index=True)
            
            # Save to CSV
            csv_file_path = os.path.join(output_folder, f"{subject_id}.csv")
            df.to_csv(csv_file_path, index=False)
            print(f"Converted {filename} to {subject_id}.csv with Channels 33-40 removed")

# Example usage
input_folder = "data_preprocessed_python"  # Path where .dat files are stored
output_folder = "data_csv"  # Path where CSV files will be saved
convert_deap_dat_to_csv(input_folder, output_folder)
