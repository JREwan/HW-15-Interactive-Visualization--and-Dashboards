# import necessary libraries
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

#################################################
# Welcome to panda world!
#################################################

@app.route("/names")
def names():
    bbb_samples = "belly_button_biodiversity_samples.csv"
    bbb_samples_df = pd.read_csv(bbb_samples, encoding = "utf-8")
    # grab the headers into a list
    sample_names =  list(bbb_samples_df)
    # get rid of the 1st header
    del sample_names[0]
    return jsonify(sample_names)

@app.route("/otu")
def otu():
    bbb_otu = "belly_button_biodiversity_otu_id.csv"
    bbb_otu_df = pd.read_csv(bbb_otu, encoding = "utf-8")
    #otu_descr_array = bbb_otu_df.lowest_taxonomic_unit_found.unique()
    otu_descr_full = bbb_otu_df["lowest_taxonomic_unit_found"].tolist()
    otu_descr = []
    #for x in otu_descr_full:
    #   if x not in otu_descr:
    #       otu_descr.append(x)
    return jsonify(otu_descr_full)

@app.route("/metadata/<sample>")
def metadata(sample):
    sample_dict = {}
    bbb_metadata = "Belly_Button_Biodiversity_Metadata.csv"
    bbb_metadata_df = pd.read_csv(bbb_metadata, encoding = "utf-8")
    #set new index
    bbb_meta_by_sampleid_df = bbb_metadata_df.set_index("SAMPLEID")
    sample_data_df = bbb_meta_by_sampleid_df.loc[[sample],["AGE", "BBTYPE", "ETHNICITY", "GENDER", "LOCATION"]] 
    sample_dict = sample_data_df.to_dict(orient='records')
    
    return jsonify(sample_dict)

@app.route("/wfreq/<sample>")
def wfreq(sample):
    wash_freq = 0
    bbb_metadata = "Belly_Button_Biodiversity_Metadata.csv"
    bbb_metadata_df = pd.read_csv(bbb_metadata, encoding = "utf-8")
    #set new index
    bbb_meta_by_sampleid_df = bbb_metadata_df.set_index("SAMPLEID")
    wash_freq = bbb_meta_by_sampleid_df.loc[sample, "WFREQ"]
    return wash_freq

@app.route("/samples/<sample>")
def samples(sample):
    otu_samples_dict = {}
    bbb_samples = "belly_button_biodiversity_samples.csv"
    bbb_samples_df = pd.read_csv(bbb_samples, encoding = "utf-8")
    results_df = bbb_samples_df[['otu_id',sample]]

    otu_list = bbb_samples_df['otu_id'].tolist()
    sample_list = bbb_samples_df[sample].tolist()
    keys = ["otu_ids", "sample_values"]
    values = [otu_list, sample_list]
    otu_samples_dict = dict(zip(keys, values))

    return jsonify(otu_samples_dict)   

if __name__ == "__main__":
    app.run()

