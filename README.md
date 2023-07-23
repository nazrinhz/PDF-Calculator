# PDF-Calculator
 Arithmetic operation on numbers contained within multiple PDF files

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/nazrinhz/pdf-calculator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PDF Calculator</h3>

  <p align="center">
  Have you ever had that moment where you have multiple PDF files that contains a single number that you need. You simply need to add up those numbers. However, when the amount of PDFs you have are more than five, it makes the job pretty cumbersome. Moreover, you would need to redo the same calculation multiple times to make sure that the numbers are correct. With this program, it reads all the files you have, locate that one number, add them up with only a few steps.
  
  This program is created as a bridge to some program or website that does not have the functionality to calculate the total.
  For example, some online banking apps only produce PDF files for transaction records. If you have multiple transaction records, how do you summate all the numbers? This program is this answer.

.
    <br />
    <a href="https://github.com/nazrinhz/pdf-calculator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nazrinhz/pdf-calculator">View Demo</a>
    ·
    <a href="https://github.com/nazrinhz/pdf-calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/nazrinhz/pdf-calculator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get this setup. You have to have a few prerequisites

### Prerequisites

Important: All PDF files must have the same format.

Install the following dependencies:
* pyPDF
  ```sh
  pip install pypdf
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nazrinhz/pdf-calculator.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use this program
1. Move or copy all the PDFs into a single directory.
2. Open `pdfcalculator.py` and setup the following parameters:
    - DIRECTORY_PATH: This is the location of the directory. Example: "C:/Users/usr/Documents/"
    - PAGE_TO_SCAN: This is the page number that contains the element we want to look for
    - TEXT_INDEX: After selecting the page, enter the text index here (will be replaced by the highlight feature)
    - CONTAINS_COMMA: Set to 1 (true) if the number contains a comma or 0 (false) otherwise. Example: 20,000
3. Run the program
```sh
python3 pdfcalculator.py
```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] Calculates the summation
- [ ] Automation on the parameter setup
- [ ] Select more than a single number
- [ ] Single-page or multi-page operation

See the [open issues](https://github.com/nazrinhz/pdf-calculator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nazrin Nazarudin - nazrinhnazarudin@gmail.com

Project Link: [https://github.com/nazrinhz/pdf-calculator](https://github.com/nazrinhz/pdf-calculator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- REFERENCES -->
## References

* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template/)
* [Pythonology What is the Best Python PDF Library](https://pythonology.eu/what-is-the-best-python-pdf-library/)
* [Count Files in Directory Python](https://java2blog.com/python-count-files-directory/)
* [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nazrinhz/pdf-calculator.svg?style=for-the-badge
[contributors-url]: https://github.com/nazrinhz/pdf-calculator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nazrinhz/pdf-calculator.svg?style=for-the-badge
[forks-url]: https://github.com/nazrinhz/pdf-calculator/network/members
[stars-shield]: https://img.shields.io/github/stars/nazrinhz/pdf-calculator.svg?style=for-the-badge
[stars-url]: https://github.com/nazrinhz/pdf-calculator/stargazers
[issues-shield]: https://img.shields.io/github/issues/nazrinhz/pdf-calculator.svg?style=for-the-badge
[issues-url]: https://github.com/nazrinhz/pdf-calculator/issues
[license-shield]: https://img.shields.io/github/license/nazrinhz/pdf-calculator.svg?style=for-the-badge
[license-url]: https://github.com/nazrinhz/pdf-calculator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/nazrinhnazarudin
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-white?style=flat-square&logo=python&logoColor=3776AB
[Python-url]: https://www.python.org/