<p align="center">
<a href="https://dashboard.decodo.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://github.com/user-attachments/assets/60bb48bd-8dcc-48b2-82c9-a218e1e4449c"></a>
</p>

[![](https://dcbadge.vercel.app/api/server/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)


<p align="center">
    <a href="https://github.com/Decodo/Decodo"> :house: Main Repository :house: </a>
</p>

### Disclaimer

The following example is a simple script showing how to utilize Decodo with Scrapy.
We suggest to research [Scrapy](https://docs.scrapy.org/en/latest/) documentation in order to continue development with this tool.

### Prerequisites

To get started with Scrapy you will first need to install it using methods provided in their documentation. [Check here for more information](https://docs.scrapy.org/en/latest/intro/install.html)

### Installation

Once you get Scrapy up and running if you have not yet, make sure that you create your project folder. Open the Terminal/Command prompt window and enter the command below:

```
scrapy startproject yourprojectname
```
<img src="https://i.imgur.com/YWqkKAS.png" alt="starting scrapy project in anaconda prompt">

When project directory is setup, you can now download our test spider code: 

1. Make sure to open the exact location in your project folder using `cd .\yourprojectname\yourprojectname\spiders\`
2. To download our example script, run command `curl https://raw.githubusercontent.com/Smartproxy/Scrapy/master/smartproxy_spider.py > smartproxy_spider.py`
3. Open the `smartproxy_spider.py` file and enter your Endpoint, Port as well as replace the Username, Password with your proxy authentication credentials.
4. Run the script using `scrapy crawl smartproxy` command.
<img src="https://i.imgur.com/fkgr0ep.png" alt="running scrapy crawl script in anaconda prompt">

Note that the code may not run if the `smartproxy_spider.py` file is in the wrong directory.

### How to check if it works?

As mentioned this script only sends a basic request to return a value from the target website.

If you have done all the steps correctly, you should see the result as `{'price': '£51.77'}` along with other actions performed by Scrapy in the Terminal window.

<img src="https://snipboard.io/0dr1Ch.jpg" alt="crawling results from target website in terminal window">

## Need help?
Email - sales@smartproxy.com
<br><a href="https://smartproxy.com">Live chat 24/7</a>


