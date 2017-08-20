# MetaLex-vagrant 
MetaLex is general tool for **lexicographics** and **metalexicographics** activities.
For current developpement version of this tool, see [MetaLex/Elvis-test](https://github.com/Levis0045/dic/tree/Elvis-test)

[![Build Status](https://travis-ci.org/claroline/Distribution.svg?branch=master)](mteprojet.fr/MetaLex)

# Requirements
MetaLex-vagrant is developped in **Python 2.7** and vagrant environment, these packages are required :

```sh
    sudo apt-get install vagrant
    sudo apt-get install virtualbox
    git clone git@github.com:Levis0045/MetaLex-vagrant.git
    cd MetaLex-vagrant
    vagrant up   #Build vagrant machine with all dependencies
    vagrant ssh  #Connect to ubuntu xenia development
    cd /vagrant
    cd Metalex-vagrant
```

# Usage

- Do this if **MetaLex folder** is in the parent of the current folder

```python
    import sys 
    sys.path.append('..')
```

- If **MetaLex folder** is in the same file or in the system path, import it.

```python
    import MetaLex
```

- Import these standard packages
```python
    import ImageFilter as f
    import MetaLex as dico
    import os, glob
``` 

- Generate real path of images dictionaries files. The input images must be scans of monolinguals dictionaries.

```python
    imagelist = []
    for imagefile in glob.glob('folder_of_Images/*.jpg') :
        name = os.getcwd()+'/'+imagefile
        imagelist.append(name)
```

- All steps below must follows as presented. **file_Rule.dic** must be build using the specific structure.

```python
    project = dico.newProject('Title of the project')
    project.setConfProject('author', 'Comment', 'Contributors')
    images  = project.MetaLex.getImages(imagelist)
    images.enhanceImages().filter(f.DETAIL)
    images.imageToText(save=True, langIn='fra')
```

- MetaLex take **file_Rule.dic** file which using  specific structure to enhance output text of OCR data (from image's files dictionnaries).

```md
    \START
    \MetaLex\project_name\type_of_project\lang\author\date
    \W
    /t'/t
    /{/f.
    /E./f.
    \C
    /i'/i
    \R
    /a-z+/ij
    \END
```

**\W** for word replacement, **\C** for caracter replacement and **\R**  for regular expression replacement.
The space between headers served to describe remplacement.

```python
   images.makeTextWell('file_Rule.dic')
   images.dicoHtml(save=False)
```

# Reference

Please don't forget to cite this work :

```latex
    @article{Mboning-Elvis,
        title  = {Quand le TAL s'empare de la métalexicographie : conception d'un outil pour le métalexicographe},
        author = {Mboning, Elvis},
        url    = {https://github.com/Levis0045/dic/},
        date   = {2017-06-20},
        shool  = {Université de Lille 3},
        year   = {2017},
        pages  = {12},
        keywords = {métalexicographie, TAL, fouille de données, extraction d'information, lecture optique, lexicographie, Xmlisation, DTD}
    }
```


