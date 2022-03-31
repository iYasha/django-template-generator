<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">

  <h3 align="center">Django Template Generator</h3>

  <p align="center">
    Template generator for production django rest framework project
    <br />
    <br />
    <a href="https://github.com/iyasha/django-template-generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/iyasha/django-template-generator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

There are many great DRF templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. That template I use at work.

This template used nginx + uwsgi + postgresql + docker.

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iyasha/django-template-generator.git
   ```
2. Go to the directory
    ```sh
   cd django-template-generator
   ```
3. Run script main.py
    ```sh
   python main.py 
   ```
4. Answer a few questions.
5. Go to the project directory
6. Run the following command
    ```sh
   mv ./config/postgres/pg-setup.sql.example ./config/postgres/pg-setup.sql
   ```
7. Run the following command
    ```sh
   mv ./.docker.env.example ./.docker.env
   ```
8. Build docker-compose.yml
   ```sh
   docker-compose -f docker-compose.dev.yml up --build
   ```
9. Go to the link [http://localhost:8080/docs](http://localhost:8080/docs) of [http://localhost:8000/docs](http://localhost:8000/docs) if u use the develop enviroment

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [ ] Add unit-test
- [ ] Remove pip, add poetry

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/iyasha/django-template-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/iyasha/django-template-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/iyasha/django-template-generator.svg?style=for-the-badge
[forks-url]: https://github.com/iyasha/django-template-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/iyasha/django-template-generator.svg?style=for-the-badge
[stars-url]: https://github.com/iyasha/django-template-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/iyasha/django-template-generator.svg?style=for-the-badge
[issues-url]: https://github.com/iyasha/django-template-generator/issues
[license-shield]: https://img.shields.io/github/license/iyasha/django-template-generator.svg?style=for-the-badge
[license-url]: https://github.com/iyasha/django-template-generator/blob/master/LICENSE.txt
