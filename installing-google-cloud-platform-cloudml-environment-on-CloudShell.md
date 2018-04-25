avinashpeyyety@cloudshell:~$ sudo pip install --upgrade pillow



Collecting pillow
  Downloading Pillow-4.0.0-cp27-cp27mu-manylinux1_x86_64.whl (5.6MB)
    100% |████████████████████████████████| 5.6MB 209kB/s 
Collecting olefile (from pillow)
  Downloading olefile-0.43.zip (119kB)
    100% |████████████████████████████████| 122kB 7.0MB/s 
Installing collected packages: olefile, pillow
  Running setup.py install for olefile ... done
Successfully installed olefile-0.43 pillow-4.0.0
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.




avinashpeyyety@cloudshell:~$ curl https://raw.githubusercontent.com/GoogleCloudPlatform/cloudml-samples/master/tools/setup_cloud_shell.sh | bash
 
 
 
 
 
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1944  100  1944    0     0   3738      0 --:--:-- --:--:-- --:--:--  3738
+ pip install --user --upgrade 'pillow>=3.4.2' --global-option=build_ext --global-option=--disable-jpeg
/usr/local/lib/python2.7/dist-packages/pip-8.1.1-py2.7.egg/pip/commands/install.py:180: UserWarning: Disabling all use of wheels due to the use of --build-options / --global-options / --install-options.
  cmdoptions.check_install_build_global(options)
Requirement already up-to-date: pillow>=3.4.2 in /usr/local/lib/python2.7/dist-packages
Requirement already up-to-date: olefile in /usr/local/lib/python2.7/dist-packages (from pillow>=3.4.2)
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
+ pip install --user --upgrade numpy pandas scikit-learn pyyaml
Collecting numpy
  Downloading numpy-1.11.3-cp27-cp27mu-manylinux1_x86_64.whl (15.4MB)
    100% |████████████████████████████████| 15.4MB 72kB/s 
Collecting pandas
  Downloading pandas-0.19.2-cp27-cp27mu-manylinux1_x86_64.whl (17.2MB)
    100% |████████████████████████████████| 17.2MB 56kB/s 
Collecting scikit-learn
  Downloading scikit_learn-0.18.1-cp27-cp27mu-manylinux1_x86_64.whl (11.6MB)
    100% |████████████████████████████████| 11.7MB 103kB/s 
Collecting pyyaml
  Downloading PyYAML-3.12.tar.gz (253kB)
    100% |████████████████████████████████| 256kB 4.3MB/s 
Collecting pytz>=2011k (from pandas)
  Downloading pytz-2016.10-py2.py3-none-any.whl (483kB)
    100% |████████████████████████████████| 491kB 2.4MB/s 
Collecting python-dateutil (from pandas)
  Downloading python_dateutil-2.6.0-py2.py3-none-any.whl (194kB)
    100% |████████████████████████████████| 194kB 5.1MB/s 
Requirement already up-to-date: six>=1.5 in /usr/local/lib/python2.7/dist-packages (from python-dateutil->pandas)
Installing collected packages: numpy, pytz, python-dateutil, pandas, scikit-learn, pyyaml
  Running setup.py install for pyyaml ... done
Successfully installed numpy pandas python-dateutil pytz pyyaml scikit-learn
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
+ pip install --user --upgrade scipy
Collecting scipy
  Downloading scipy-0.18.1-cp27-cp27mu-manylinux1_x86_64.whl (40.3MB)
    100% |████████████████████████████████| 40.3MB 6.9kB/s 
Installing collected packages: scipy
Successfully installed scipy-0.18.1
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
+ pip install --user --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/debian/jessie/tensorflow-0.11.0-cp27-none-linux_x86_64.whl
Collecting tensorflow==0.11.0 from https://storage.googleapis.com/tensorflow/linux/cpu/debian/jessie/tensorflow-0.11.0-cp27-none-linux_x86_64.whl
  Downloading https://storage.googleapis.com/tensorflow/linux/cpu/debian/jessie/tensorflow-0.11.0-cp27-none-linux_x86_64.whl (40.2MB)
    100% |████████████████████████████████| 40.2MB 2.6kB/s 
Collecting mock>=2.0.0 (from tensorflow==0.11.0)
  Downloading mock-2.0.0-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 1.3MB/s 
Requirement already up-to-date: six>=1.10.0 in /usr/local/lib/python2.7/dist-packages (from tensorflow==0.11.0)
Requirement already up-to-date: numpy>=1.11.0 in ./.local/lib/python2.7/site-packages (from tensorflow==0.11.0)
Collecting wheel (from tensorflow==0.11.0)
  Downloading wheel-0.29.0-py2.py3-none-any.whl (66kB)
    100% |████████████████████████████████| 71kB 1.4MB/s 
Collecting protobuf==3.0.0 (from tensorflow==0.11.0)
  Downloading protobuf-3.0.0-py2.py3-none-any.whl (342kB)
    100% |████████████████████████████████| 348kB 564kB/s 
Collecting funcsigs>=1 (from mock>=2.0.0->tensorflow==0.11.0)
  Downloading funcsigs-1.0.2-py2.py3-none-any.whl
Collecting pbr>=0.11 (from mock>=2.0.0->tensorflow==0.11.0)
  Downloading pbr-1.10.0-py2.py3-none-any.whl (96kB)
    100% |████████████████████████████████| 102kB 487kB/s 
Collecting setuptools (from protobuf==3.0.0->tensorflow==0.11.0)
  Downloading setuptools-32.3.1-py2.py3-none-any.whl (479kB)
    100% |████████████████████████████████| 481kB 386kB/s 
Installing collected packages: funcsigs, pbr, mock, wheel, setuptools, protobuf, tensorflow
Successfully installed funcsigs-1.0.2 mock-2.0.0 pbr-1.10.0 protobuf-3.0.0 setuptools-32.3.1 tensorflow-0.11.0 wheel-0.29.0
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
+ pip install --user --upgrade https://storage.googleapis.com/cloud-ml/sdk/cloudml.latest.tar.gz
Collecting https://storage.googleapis.com/cloud-ml/sdk/cloudml.latest.tar.gz
  Downloading https://storage.googleapis.com/cloud-ml/sdk/cloudml.latest.tar.gz (75kB)
    100% |████████████████████████████████| 81kB 4.4MB/s 
Collecting oauth2client==2.2.0 (from cloudml==0.1.7a0)
  Downloading oauth2client-2.2.0.tar.gz (70kB)
    100% |████████████████████████████████| 71kB 332kB/s 
Requirement already up-to-date: six>=1.10.0 in /usr/local/lib/python2.7/dist-packages (from cloudml==0.1.7a0)
Collecting google-cloud-dataflow>=0.4.2 (from cloudml==0.1.7a0)
  Downloading google-cloud-dataflow-0.4.4.zip (619kB)
    100% |████████████████████████████████| 624kB 382kB/s 
Collecting bs4>=0.0.1 (from cloudml==0.1.7a0)
  Downloading bs4-0.0.1.tar.gz
Requirement already up-to-date: numpy>=1.10.4 in ./.local/lib/python2.7/site-packages (from cloudml==0.1.7a0)
Collecting pillow==3.4.1 (from cloudml==0.1.7a0)
  Downloading Pillow-3.4.1-cp27-cp27mu-manylinux1_x86_64.whl (5.6MB)
    100% |████████████████████████████████| 5.6MB 34kB/s 
Collecting dpkt>=1.8.7 (from cloudml==0.1.7a0)
  Downloading dpkt-1.8.8-py2-none-any.whl (119kB)
    100% |████████████████████████████████| 122kB 489kB/s 
Collecting nltk>=3.2.1 (from cloudml==0.1.7a0)
  Downloading nltk-3.2.2.tar.gz (1.2MB)
    100% |████████████████████████████████| 1.2MB 101kB/s 
Requirement already up-to-date: httplib2>=0.9.1 in /usr/local/lib/python2.7/dist-packages (from oauth2client==2.2.0->cloudml==0.1.7a0)
Requirement already up-to-date: pyasn1>=0.1.7 in /usr/local/lib/python2.7/dist-packages (from oauth2client==2.2.0->cloudml==0.1.7a0)
Requirement already up-to-date: pyasn1-modules>=0.0.5 in /usr/local/lib/python2.7/dist-packages (from oauth2client==2.2.0->cloudml==0.1.7a0)
Requirement already up-to-date: rsa>=3.1.4 in /usr/local/lib/python2.7/dist-packages (from oauth2client==2.2.0->cloudml==0.1.7a0)
Collecting avro<2.0.0,>=1.7.7 (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading avro-1.8.1.tar.gz (44kB)
    100% |████████████████████████████████| 51kB 8.3MB/s 
Collecting dill<0.3,>=0.2.5 (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading dill-0.2.5.tgz (60kB)
    100% |████████████████████████████████| 61kB 8.2MB/s 
Collecting google-apitools<1.0.0,>=0.5.2 (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading google-apitools-0.5.6.zip (320kB)
    100% |████████████████████████████████| 327kB 478kB/s 
Collecting googledatastore==6.4.1 (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading googledatastore-6.4.1.tar.gz
Requirement already up-to-date: mock<3.0.0,>=1.0.1 in ./.local/lib/python2.7/site-packages (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
Requirement already up-to-date: protobuf==3.0.0 in ./.local/lib/python2.7/site-packages (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
Collecting protorpc<0.12,>=0.9.1 (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading protorpc-0.11.1-py2-none-any.whl (134kB)
    100% |████████████████████████████████| 143kB 530kB/s 
Collecting python-gflags<4.0.0,>=2.0 (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading python-gflags-3.1.0.tar.gz (52kB)
    100% |████████████████████████████████| 61kB 8.5MB/s 
Requirement already up-to-date: pyyaml<4.0.0,>=3.10 in ./.local/lib/python2.7/site-packages (from google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
Collecting beautifulsoup4 (from bs4>=0.0.1->cloudml==0.1.7a0)
  Downloading beautifulsoup4-4.5.3-py2-none-any.whl (85kB)
    100% |████████████████████████████████| 92kB 7.0MB/s 
Requirement already up-to-date: setuptools>=18.5 in ./.local/lib/python2.7/site-packages (from google-apitools<1.0.0,>=0.5.2->google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
Collecting proto-google-datastore-v1==1.3.1 (from googledatastore==6.4.1->google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
  Downloading proto-google-datastore-v1-1.3.1.tar.gz
Requirement already up-to-date: funcsigs>=1 in ./.local/lib/python2.7/site-packages (from mock<3.0.0,>=1.0.1->google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
Requirement already up-to-date: pbr>=0.11 in ./.local/lib/python2.7/site-packages (from mock<3.0.0,>=1.0.1->google-cloud-dataflow>=0.4.2->cloudml==0.1.7a0)
Building wheels for collected packages: oauth2client, google-cloud-dataflow, bs4, nltk, avro, dill, google-apitools, googledatastore, python-gflags, proto-google-datastore-v1
  Running setup.py bdist_wheel for oauth2client ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/af/ae/a0/a103f5040adac297bae0c0b4a4e45f291be4c5ea8ca161fe42
  Running setup.py bdist_wheel for google-cloud-dataflow ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/a6/b7/72/c6967943092aee094eb2ba783f7f94a2ecf01ceb676ae79a71
  Running setup.py bdist_wheel for bs4 ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/84/67/d4/9e09d9d5adede2ee1c7b7e8775ba3fbb04d07c4f946f0e4f11
  Running setup.py bdist_wheel for nltk ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/42/b5/27/718985cd9719e8a44a405d264d98214c7a607fb65f3a006f28
  Running setup.py bdist_wheel for avro ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/48/ab/c0/24e702060d5a877cb970047248c9ea5d531067915324128b58
  Running setup.py bdist_wheel for dill ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/4c/61/4b/fe80508bd8f3102b75998dfbc1202a0153838a460c29de4d54
  Running setup.py bdist_wheel for google-apitools ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/2d/57/b5/c5ed1dee85690a7e89fc14f9b89b58d6b5e6711e8f641d0b2b
  Running setup.py bdist_wheel for googledatastore ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/f1/5d/47/db63b9f7453568fd62dbab735fbde511f9cb529dd9c519ef14
  Running setup.py bdist_wheel for python-gflags ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/2c/1c/a6/0fa8331f3c6116e552701fb40fc8d467f6f5fe5b9eea75f176
  Running setup.py bdist_wheel for proto-google-datastore-v1 ... done
  Stored in directory: /home/avinashpeyyety/.cache/pip/wheels/03/4f/81/cfab89a365b843d9519ab504776dd27f3a4449dada5002ab8c
Successfully built oauth2client google-cloud-dataflow bs4 nltk avro dill google-apitools googledatastore python-gflags proto-google-datastore-v1
Installing collected packages: oauth2client, avro, dill, google-apitools, proto-google-datastore-v1, googledatastore, protorpc, python-gflags, google-cloud-dataflow, beautifulsoup4, bs4, pillow, dpkt, nltk, cloudml
  Running setup.py install for cloudml ... done
Successfully installed avro-1.8.1 beautifulsoup4-4.5.3 bs4-0.0.1 cloudml-0.1.7a0 dill-0.2.5 dpkt-1.8.8 google-apitools-0.5.6 google-cloud-dataflow-0.4.4 googledatastore-6.4.1 nltk-3.2.2 oauth2client-2.2.0 pillow-3.4.1 proto-google-datastore-v1-1.3.1 protorpc-0.11.1 python-gflags-3.1.0
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
+ echo 'export PATH=${HOME}/.local/bin:${PATH}'
+ mkdir -p /home/avinashpeyyety/google-cloud-ml
+ cd /home/avinashpeyyety/google-cloud-ml
+ '[' -d samples ']'
+ curl -L -o cloudml-samples.zip https://github.com/GoogleCloudPlatform/cloudml-samples/archive/master.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   140    0   140    0     0    151      0 --:--:-- --:--:-- --:--:--   151
100  100k  100  100k    0     0  45283      0  0:00:02  0:00:02 --:--:-- 89938
+ unzip cloudml-samples.zip
Archive:  cloudml-samples.zip
229abe67d862c5368fae27c5bdbd34fdf34321bc
   creating: cloudml-samples-master/
  inflating: cloudml-samples-master/CONTRIBUTING.md  
  inflating: cloudml-samples-master/LICENSE  
  inflating: cloudml-samples-master/README.md  
   creating: cloudml-samples-master/flowers/
  inflating: cloudml-samples-master/flowers/README.md  
  inflating: cloudml-samples-master/flowers/images_to_json.py  
  inflating: cloudml-samples-master/flowers/sample.sh  
  inflating: cloudml-samples-master/flowers/setup.py  
   creating: cloudml-samples-master/flowers/trainer/
  inflating: cloudml-samples-master/flowers/trainer/__init__.py  
  inflating: cloudml-samples-master/flowers/trainer/model.py  
  inflating: cloudml-samples-master/flowers/trainer/preprocess.py  
  inflating: cloudml-samples-master/flowers/trainer/task.py  
  inflating: cloudml-samples-master/flowers/trainer/util.py  
   creating: cloudml-samples-master/iris/
  inflating: cloudml-samples-master/iris/README.md  
  inflating: cloudml-samples-master/iris/data_predict.csv  
  inflating: cloudml-samples-master/iris/pipeline.py  
  inflating: cloudml-samples-master/iris/preprocess.py  
  inflating: cloudml-samples-master/iris/setup.py  
   creating: cloudml-samples-master/iris/trainer/
  inflating: cloudml-samples-master/iris/trainer/__init__.py  
  inflating: cloudml-samples-master/iris/trainer/model.py  
  inflating: cloudml-samples-master/iris/trainer/task.py  
  inflating: cloudml-samples-master/iris/trainer/util.py  
   creating: cloudml-samples-master/mnist/
  inflating: cloudml-samples-master/mnist/README.md  
   creating: cloudml-samples-master/mnist/deployable/
   creating: cloudml-samples-master/mnist/deployable/data/
  inflating: cloudml-samples-master/mnist/deployable/data/eval_sample.tensor.json  
  inflating: cloudml-samples-master/mnist/deployable/data/predict_sample.tensor.json  
   creating: cloudml-samples-master/mnist/deployable/trainer/
  inflating: cloudml-samples-master/mnist/deployable/trainer/__init__.py  
  inflating: cloudml-samples-master/mnist/deployable/trainer/input_data.py  
  inflating: cloudml-samples-master/mnist/deployable/trainer/task.py  
   creating: cloudml-samples-master/mnist/distributed/
   creating: cloudml-samples-master/mnist/distributed/data/
  inflating: cloudml-samples-master/mnist/distributed/data/eval_sample.tensor.json  
  inflating: cloudml-samples-master/mnist/distributed/data/eval_sample.tfrecord  
  inflating: cloudml-samples-master/mnist/distributed/local_predict.py  
   creating: cloudml-samples-master/mnist/distributed/trainer/
  inflating: cloudml-samples-master/mnist/distributed/trainer/__init__.py  
  inflating: cloudml-samples-master/mnist/distributed/trainer/model.py  
  inflating: cloudml-samples-master/mnist/distributed/trainer/task.py  
  inflating: cloudml-samples-master/mnist/distributed/trainer/util.py  
   creating: cloudml-samples-master/mnist/hptuning/
   creating: cloudml-samples-master/mnist/hptuning/trainer/
  inflating: cloudml-samples-master/mnist/hptuning/trainer/__init__.py  
  inflating: cloudml-samples-master/mnist/hptuning/trainer/model.py  
  inflating: cloudml-samples-master/mnist/hptuning/trainer/task.py  
  inflating: cloudml-samples-master/mnist/hptuning/trainer/util.py  
   creating: cloudml-samples-master/mnist/trainable/
   creating: cloudml-samples-master/mnist/trainable/trainer/
  inflating: cloudml-samples-master/mnist/trainable/trainer/__init__.py  
  inflating: cloudml-samples-master/mnist/trainable/trainer/task.py  
   creating: cloudml-samples-master/tools/
  inflating: cloudml-samples-master/tools/check_environment.py  
  inflating: cloudml-samples-master/tools/setup_cloud_shell.sh  
  inflating: cloudml-samples-master/tools/setup_docker.sh  
+ mv cloudml-samples-master/ samples/
+ echo 'Success! Your environment has the required tools and dependencies.'
Success! Your environment has the required tools and dependencies.
avinashpeyyety@cloudshell:~$ 
