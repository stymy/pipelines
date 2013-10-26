import os
import surfer.io as surf
subjects = [
'mark'
]

exclude_subjects = []
subjects = list(set(subjects) - set(exclude_subjects))

analysis_subjects = ['mark'
]

sessions = ['session1','session2','session3','session4','session5']
analysis_sessions = ['session1','session2','session3','session4','session5']

workingdir = "/scr/ilz1/data/mark"
resultsdir = "/scr/ilz1/data/mark_results"
freesurferdir = '/scr/ilz1/data'

#slicetime_file = '/scr/ilz1/data/NKI_High/scripts/sliceTime2.txt'
rois = [(26,58,0), (-26,58,0), (14,66,0), (-14,66,0), (6,58,0), (-6,58,0)]

def getvertices(hemi,freesurferdir):
    labellist = [1, 5, 13, 14, 15, 16, 24, 31, 32, 39, 40, 53, 54, 55, 63, 64, 65, 71]
    [vertices,colortable,names] = surf.read_annot(freesurferdir+'/fsaverage4/label/'+hemi[-2:]+'.aparc.a2009s.annot', orig_ids=True)
    chosenvertices = list()
    for j, value in enumerate(vertices) :
        for i, index in enumerate(labellist) :
            if colortable[index][4]==value :
                chosenvertices.append(j)
    return chosenvertices

lhvertices = getvertices('lh',freesurferdir)
rhvertices = getvertices('rh',freesurferdir)

hemispheres = ['lh', 'rh']
similarity_types = ['eta2', 'spat', 'temp']
cluster_types = ['spectral', 'hiercluster', 'kmeans', 'dbscan']
n_clusters = [7]