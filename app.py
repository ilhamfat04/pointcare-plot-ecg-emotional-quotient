from flask import Flask, render_template,redirect, url_for, request, flash
from werkzeug.utils import secure_filename
import os
import pandas as pd
import numpy as np
from twoAverage import Detectors
import pywt
import pathlib
import scipy.signal as signal
from biosppy import ecg
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

UPLOAD_FOLDER= 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.secret_key = "mysecretkey"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/ekstraksi_fitur")
def ekstraksi_fitur():
    
    return render_template('ekstraksi_fitur.html')

@app.route("/peak_detection")
def peak_detection():
    
    
    return render_template('peak_detection.html')

@app.route("/plot_peak_pre")
def plot_peak_pre():
    # plot peak detection
    # data source location
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data/'
    file = 'S01_01_pre'
    folder_peak = 'peak_results/'

    # reading data
    data = np.genfromtxt(folder+file+'.csv')

    # define frequency sampling
    fs = 50

    # peak detection process
    detect = Detectors(fs)
    r_peaks = detect.two_average_detector(data[:1000])
    r_peaks_temp = detect.two_average_detector(data)
    
    # creating peak_subject.txt data
    wrt_peak = open(folder_peak+"peak_"+file+".csv","w")
    wrt_peak.write("position"+","+"peak"+"\n")
    for i in r_peaks_temp:
        wrt_peak.write(str(i)+","+str(int(data[i]))+"\n")
    wrt_peak.close()
    # plot peak detection
    plt.figure()
    plt.plot(data[:1000])
    plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/plotpre.png')
    return redirect(url_for('peak_detection'))

@app.route("/plot_peak_no_point_pre")
def plot_peak_no_point_pre():
    # plot peak detection
    # data source location
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data/'
    file = 'S01_01_pre'
    folder_peak = 'peak_results/'

    # reading data
    data = np.genfromtxt(folder+file+'.csv')

    # define frequency sampling
    fs = 50

    # peak detection process
    detect = Detectors(fs)
    r_peaks = detect.two_average_detector(data[:1000])
    
    # creating peak_subject.txt data
    wrt_peak = open(folder_peak+"peak_"+file+".csv","w")
    wrt_peak.write("position"+","+"peak"+"\n")
    for i in r_peaks:
        wrt_peak.write(str(i)+","+str(int(data[i]))+"\n")
    wrt_peak.close()
    # plot peak detection
    plt.figure()
    plt.plot(data[:1000])
    # plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/plotnopointpre.png')
    return redirect(url_for('peak_detection'))

@app.route("/plot_peak_on")
def plot_peak_on():
    # plot peak detection
    # data source location
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data/'
    file = 'S01_01_on'
    folder_peak = 'peak_results/'

    # reading data
    data = np.genfromtxt(folder+file+'.csv')

    # define frequency sampling
    fs = 50

    # peak detection process
    detect = Detectors(fs)
    r_peaks = detect.two_average_detector(data[:1000])
    r_peaks_temp = detect.two_average_detector(data)
    
    # creating peak_subject.txt data
    wrt_peak = open(folder_peak+"peak_"+file+".csv","w")
    wrt_peak.write("position"+","+"peak"+"\n")
    for i in r_peaks_temp:
        wrt_peak.write(str(i)+","+str(int(data[i]))+"\n")
    wrt_peak.close()
    # plot peak detection
    plt.figure()
    plt.plot(data[:1000])
    plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/ploton.png')
    return redirect(url_for('peak_detection'))

@app.route("/plot_peak_no_point_on")
def plot_peak_no_point_on():
    # plot peak detection
    # data source location
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data/'
    file = 'S01_01_on'
    folder_peak = 'peak_results/'

    # reading data
    data = np.genfromtxt(folder+file+'.csv')

    # define frequency sampling
    fs = 50

    # peak detection process
    detect = Detectors(fs)
    r_peaks = detect.two_average_detector(data[:1000])
    
    # creating peak_subject.txt data
    wrt_peak = open(folder_peak+"peak_"+file+".csv","w")
    wrt_peak.write("position"+","+"peak"+"\n")
    for i in r_peaks:
        wrt_peak.write(str(i)+","+str(int(data[i]))+"\n")
    wrt_peak.close()
    # plot peak detection
    plt.figure()
    plt.plot(data[:1000])
    # plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/plotnopointon.png')
    return redirect(url_for('peak_detection'))

@app.route("/plot_peak_post")
def plot_peak_post():
    # plot peak detection
    # data source location
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data/'
    file = 'S01_01_post'
    folder_peak = 'peak_results/'

    # reading data
    data = np.genfromtxt(folder+file+'.csv')

    # define frequency sampling
    fs = 50

    # peak detection process
    detect = Detectors(fs)
    r_peaks = detect.two_average_detector(data[:1000])
    r_peaks_temp = detect.two_average_detector(data)
    
    # creating peak_subject.txt data
    wrt_peak = open(folder_peak+"peak_"+file+".csv","w")
    wrt_peak.write("position"+","+"peak"+"\n")
    for i in r_peaks_temp:
        wrt_peak.write(str(i)+","+str(int(data[i]))+"\n")
    wrt_peak.close()
    # plot peak detection
    plt.figure()
    plt.plot(data[:1000])
    plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/plotpost.png')
    return redirect(url_for('peak_detection'))

@app.route("/plot_peak_no_point_post")
def plot_peak_no_point_post():
    # plot peak detection
    # data source location
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/raw_data/'
    file = 'S01_01_post'
    folder_peak = 'peak_results/'

    # reading data
    data = np.genfromtxt(folder+file+'.csv')

    # define frequency sampling
    fs = 50

    # peak detection process
    detect = Detectors(fs)
    r_peaks = detect.two_average_detector(data[:1000])
    
    # creating peak_subject.txt data
    wrt_peak = open(folder_peak+"peak_"+file+".csv","w")
    wrt_peak.write("position"+","+"peak"+"\n")
    for i in r_peaks:
        wrt_peak.write(str(i)+","+str(int(data[i]))+"\n")
    wrt_peak.close()
    # plot peak detection
    plt.figure()
    plt.plot(data[:1000])
    # plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected R-peaks')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/plotnopointpost.png')
    return redirect(url_for('peak_detection'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/import_data_pre', methods=['GET', 'POST'])
def import_data_pre():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            nama_file = 'S01_01_pre.csv'
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_file))
            return redirect(url_for('peak_detection', name=filename, ))
    return redirect(url_for('peak_detection'))

@app.route('/import_data_on', methods=['GET', 'POST'])
def import_data_on():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            nama_file = 'S01_01_on.csv'
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_file))
            return redirect(url_for('peak_detection', name=filename, ))
    return redirect(url_for('peak_detection'))

@app.route('/import_data_post', methods=['GET', 'POST'])
def import_data_post():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            nama_file = 'S01_01_post.csv'
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_file))
            return redirect(url_for('peak_detection', name=filename, ))
    return redirect(url_for('peak_detection'))


@app.route("/rr_extraction_pre")
def rr_extraction_pre():
    # sFolder=source folder, dFolder=destination folder 
    sFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/peak_results/'
    dFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(sFolder):
        for file in f:
            if '.csv' in file:
                (name,ext) = os.path.splitext(file)
                dataset = pd.read_csv(sFolder+name+".csv")
                rr = np.diff(dataset['position'])
                wrt_rr = open(dFolder+ "rri_"+name[5:]+".csv","w")
                for i in rr:
                    wrt_rr.write(str(i) + "\n")
                wrt_rr.close()
                
            print(file+' done.')
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'
    file = 'rri_S01_01_pre'
    flash("Great !!!, Feature Extraction Done.")
    # reading data
    data = np.genfromtxt(folder+file+'.csv')
    
    plt.figure()
    plt.plot(data)
    # plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected RRI Result')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/rrresultpre.png')
    return redirect(url_for('ekstraksi_fitur'))

@app.route("/rr_extraction_on")
def rr_extraction_on():
    # sFolder=source folder, dFolder=destination folder 
    sFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/peak_results/'
    dFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(sFolder):
        for file in f:
            if '.csv' in file:
                (name,ext) = os.path.splitext(file)
                dataset = pd.read_csv(sFolder+name+".csv")
                rr = np.diff(dataset['position'])
                wrt_rr = open(dFolder+ "rri_"+name[5:]+".csv","w")
                for i in rr:
                    wrt_rr.write(str(i) + "\n")
                wrt_rr.close()
            print(file+' done.')
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'
    file = 'rri_S01_01_on'
    flash("Great !!!, Feature Extraction Done.")
    # reading data
    data = np.genfromtxt(folder+file+'.csv')
    
    plt.figure()
    plt.plot(data)
    # plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected RRI Result')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/rrresulton.png')
    return redirect(url_for('ekstraksi_fitur'))

@app.route("/rr_extraction_post")
def rr_extraction_post():
    # sFolder=source folder, dFolder=destination folder 
    sFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/peak_results/'
    dFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(sFolder):
        for file in f:
            if '.csv' in file:
                (name,ext) = os.path.splitext(file)
                dataset = pd.read_csv(sFolder+name+".csv")
                rr = np.diff(dataset['position'])
                wrt_rr = open(dFolder+ "rri_"+name[5:]+".csv","w")
                for i in rr:
                    wrt_rr.write(str(i) + "\n")
                wrt_rr.close()
            print(file+' done.')
    folder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'
    file = 'rri_S01_01_post'
    flash("Great !!!, Feature Extraction Done.")
    # reading data
    data = np.genfromtxt(folder+file+'.csv')
    
    plt.figure()
    plt.plot(data)
    # plt.plot(r_peaks, data[r_peaks], 'ro')
    plt.title('Detected RRI Result')
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/rrresultpost.png')
    return redirect(url_for('ekstraksi_fitur'))


@app.route("/pointcare_plot")
def pointcare_plot() :
          
    
     return render_template('pointcare_plot.html')

@app.route("/display_pointcare_plot_pre")
def display_pointcare_plot_pre() :
    
    # selecting data
    sFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'
    # dFolder = 'D:/Brankas/Medical Informatics/4th Thesis/Multi Parameter Stroke/Progress Meeeting/Poincare Plot/sit-stand/'

    file = 'rri_S01_01_pre'

    rr = np.genfromtxt(sFolder+file+".csv",delimiter="")

    x = rr[:-1]
    y = rr[1:]

    xcenter, ycenter = np.average(x), np.average(y)
    center = (xcenter, ycenter)

    x1,y1 = [],[]

    for i in range(len(x)):
        x1.append((x[i]-y[i])/np.sqrt(2))
        y1.append((x[i]+y[i])/np.sqrt(2))

    sd1, sd2 = np.sqrt(np.var(x1)), np.sqrt(np.var(y1))

    e = Ellipse(center, 2*sd2, 2*sd1, 45.0)

    fig, ax = plt.subplots(figsize=(6,6),sharex=True,sharey=True)
    ax.add_artist(e)
    # e.set_alpha(0.5)
    e.set_facecolor('black')

    plt.scatter(x,y,color='silver',edgecolors='black')
    plt.scatter(xcenter, ycenter, color='white', marker='.')

    plt.xlabel('RRI (ms)',fontsize=14)
    plt.ylabel('RRI+1 (ms)',fontsize=14)
    plt.tick_params(labelsize='large')
    plt.xlim(10,40)
    plt.ylim(10,40)
    # plt.suptitle(file[4:])
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/pointcare_plotpre.png')
    
    return redirect(url_for('pointcare_plot'))

@app.route("/display_pointcare_plot_on")
def display_pointcare_plot_on() :
    
    # selecting data
    sFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'
    # dFolder = 'D:/Brankas/Medical Informatics/4th Thesis/Multi Parameter Stroke/Progress Meeeting/Poincare Plot/sit-stand/'

    file = 'rri_S01_01_on'

    rr = np.genfromtxt(sFolder+file+".csv",delimiter="")

    x = rr[:-1]
    y = rr[1:]

    xcenter, ycenter = np.average(x), np.average(y)
    center = (xcenter, ycenter)

    x1,y1 = [],[]

    for i in range(len(x)):
        x1.append((x[i]-y[i])/np.sqrt(2))
        y1.append((x[i]+y[i])/np.sqrt(2))

    sd1, sd2 = np.sqrt(np.var(x1)), np.sqrt(np.var(y1))

    e = Ellipse(center, 2*sd2, 2*sd1, 45.0)

    fig, ax = plt.subplots(figsize=(6,6),sharex=True,sharey=True)
    ax.add_artist(e)
    # e.set_alpha(0.5)
    e.set_facecolor('black')

    plt.scatter(x,y,color='silver',edgecolors='black')
    plt.scatter(xcenter, ycenter, color='white', marker='.')

    plt.xlabel('RRI (ms)',fontsize=14)
    plt.ylabel('RRI+1 (ms)',fontsize=14)
    plt.tick_params(labelsize='large')
    plt.xlim(10,40)
    plt.ylim(10,40)
    # plt.suptitle(file[4:])
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/pointcare_ploton.png')
    
    return redirect(url_for('pointcare_plot'))
 
@app.route("/display_pointcare_plot_post")
def display_pointcare_plot_post() :
    
    # selecting data
    sFolder = 'D:/Kampus/SMT8/belajar/Data Processing1/rr_results/'
    # dFolder = 'D:/Brankas/Medical Informatics/4th Thesis/Multi Parameter Stroke/Progress Meeeting/Poincare Plot/sit-stand/'

    file = 'rri_S01_01_post'

    rr = np.genfromtxt(sFolder+file+".csv",delimiter="")

    x = rr[:-1]
    y = rr[1:]

    xcenter, ycenter = np.average(x), np.average(y)
    center = (xcenter, ycenter)

    x1,y1 = [],[]

    for i in range(len(x)):
        x1.append((x[i]-y[i])/np.sqrt(2))
        y1.append((x[i]+y[i])/np.sqrt(2))

    sd1, sd2 = np.sqrt(np.var(x1)), np.sqrt(np.var(y1))

    e = Ellipse(center, 2*sd2, 2*sd1, 45.0)

    fig, ax = plt.subplots(figsize=(6,6),sharex=True,sharey=True)
    ax.add_artist(e)
    # e.set_alpha(0.5)
    e.set_facecolor('black')

    plt.scatter(x,y,color='silver',edgecolors='black')
    plt.scatter(xcenter, ycenter, color='white', marker='.')

    plt.xlabel('RRI (ms)',fontsize=14)
    plt.ylabel('RRI+1 (ms)',fontsize=14)
    plt.tick_params(labelsize='large')
    plt.xlim(10,40)
    plt.ylim(10,40)
    # plt.suptitle(file[4:])
    plt.savefig('D:/Kampus/SMT8/belajar/Data Processing1/static/images/pointcare_plotpost.png')
    
    return redirect(url_for('pointcare_plot'))

if __name__ == "__main__":
    app.run(debug=True)