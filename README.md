<h1 align="center">⚡Listreqs</h1>
<p align="center">
<a href=""><img alt="Contributions Welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen?style=for-the-badge&labelColor=black&logo=github"></a>
<br/>
<img alt="GitHub" src="https://img.shields.io/github/license/soumya997/Listreqs?style=for-the-badge">

</p>
 
<p align="center">

 <img src="https://forthebadge.com/images/badges/built-with-love.svg"> <img src="https://forthebadge.com/images/badges/made-with-python.svg"> <img src="https://forthebadge.com/images/badges/open-source.svg"> <img src="https://forthebadge.com/images/badges/made-with-reason.svg">

</p>

<i>
<strong><code>Listreqs</code></strong> is a simple <code>requirements.txt</code> generator. <strong><code>It's an alternative to pipreqs</code></strong>. Where in Pipreqs, it helps you to Generate requirements.txt file for any project based on imports, but in Listreqs you need to create a <strong>virtual environment first</strong>, and do your required installations there. And when you need to create your <strong><code>requirements.txt</code></strong> use Listreqs.
</i>

</p>
<br>

<!-- ![ezgif-6-11ef5ffcbfc5](https://user-images.githubusercontent.com/54326088/136756679-5c8328fd-7fda-462e-8d3a-fd4e1c063553.gif)
![libreqs1](https://user-images.githubusercontent.com/40317114/136805935-ed7a07a2-8406-44e2-8ec6-50296cc9f7d1.gif)
 -->
| Using shell script             |  Using python script |
:-------------------------:|:-------------------------:
![](https://im.ezgif.com/tmp/ezgif-1-c4babba09e56.gif)  |  ![](https://user-images.githubusercontent.com/54326088/136756679-5c8328fd-7fda-462e-8d3a-fd4e1c063553.gif)



# How to use:
### `Use the only python script:`
1. Create your virtual env, 
    ```
    - pip install virtualenv
    - mkdir TextGenEnv
    - virtualenv TextGenEnv
    - activate the env:  
      + for cmd -> TextGenEnv\Scripts\activate 
      + (for git bash, source ./Scripts/activate)
      + (for linux terminal, source TextGenEnv/bin/activate)
    ```
2. do your required installations there
3. And when you need to create your requirements.txt do these steps,
    - activate the environment using above command
    - `pip list > requirements.txt` -> it will put the output of the `pip list` command inside the `requirements.txt`
    - `python listreqs.py`  and give the path of the previously created `requirements.txt`
4. Boom!!!


### `Use only shell script:`
1. Create your virtual env, 
    ```
    - pip install virtualenv
    - mkdir TextGenEnv
    - virtualenv TextGenEnv
    - activate the env:  
      + TextGenEnv\Scripts\activate 
      + (for bash source ./Scripts/activate)
    ```
2. do your required installations there
3. And when you need to create your requirements.txt do these steps,
    - `sh listreqs.sh` and pass the file name `requirements.txt`.
    - Boom!!!
    - **heads up while using the shell script**,
       + Usage:
         1. Can pass in as a positional(command line) argument:
         ```
         bash listreqs.sh reqs.txt
         ```

         2. Can input the file name from the prompt after running the shell script
         ```
         bash listreqs.sh
         Enter the requirements file name : reqs.txt
         ```

         3. Not passing any input will lead to the creation of a default file called `requirements.txt`.
         ```
         bash listreqs.sh
         Enter the requirements file name : 
         ```

# Know more about How to create virtual environment:
<a target="_blank" href="https://github-readme-medium-recent-article.vercel.app/medium/@khanfarhan10/3"><img src="https://github-readme-medium-recent-article.vercel.app/medium/@khanfarhan10/3" alt="Recent Article 3"> 

 # todos:

- [x] create a single shell script to get the job done.
- [ ] Use the python script to create a python library. Is should be like a shell command,like doing `python Listreqs` after activating the virtual environment should create a `requirements.txt` with all the installed package name and verison inside the current directory.  
