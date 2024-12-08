Title: GitHub - jina-ai/reader: Convert any URL to an LLM-friendly input with a simple prefix https://r.jina.ai/

URL Source: https://github.com/jina-ai/reader

Markdown Content:
Reader
------

[](https://github.com/jina-ai/reader#reader)

Your LLMs deserve better input.

Reader does two things:

*   **Read**: It converts any URL to an **LLM-friendly** input with `https://r.jina.ai/https://your.url`. Get improved output for your agent and RAG systems at no cost.
*   **Search**: It searches the web for a given query with `https://s.jina.ai/your+query`. This allows your LLMs to access the latest world knowledge from the web.

Check out [the live demo](https://jina.ai/reader#demo)

Or just visit these URLs (**Read**) [https://r.jina.ai/https://github.com/jina-ai/reader](https://r.jina.ai/https://github.com/jina-ai/reader), (**Search**) [https://s.jina.ai/Who%20will%20win%202024%20US%20presidential%20election%3F](https://s.jina.ai/Who%20will%20win%202024%20US%20presidential%20election%3F) and see yourself.

> Feel free to use Reader API in production. It is free, stable and scalable. We are maintaining it actively as one of the core products of Jina AI. [Check out rate limit](https://jina.ai/reader#pricing)

[![Image 7: image](https://private-user-images.githubusercontent.com/2041322/324206629-2067c7a2-c12e-4465-b107-9a16ca178d41.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM2MDg3NTcsIm5iZiI6MTczMzYwODQ1NywicGF0aCI6Ii8yMDQxMzIyLzMyNDIwNjYyOS0yMDY3YzdhMi1jMTJlLTQ0NjUtYjEwNy05YTE2Y2ExNzhkNDEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTIwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEyMDdUMjE1NDE3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9Y2E3NGU2OGY5NTlkNGEzOGNkYjc2Y2YxYWM3ZWIwZGJkNzRkMTY3ZTE1ZDcxYmEwZTg5MDAwOTNlYjU5YzJkZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.2dS48YOhoUyU6A4YoZMQZebFGzzSRpeZVQEp0kG7khs)](https://private-user-images.githubusercontent.com/2041322/324206629-2067c7a2-c12e-4465-b107-9a16ca178d41.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM2MDg3NTcsIm5iZiI6MTczMzYwODQ1NywicGF0aCI6Ii8yMDQxMzIyLzMyNDIwNjYyOS0yMDY3YzdhMi1jMTJlLTQ0NjUtYjEwNy05YTE2Y2ExNzhkNDEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTIwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEyMDdUMjE1NDE3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9Y2E3NGU2OGY5NTlkNGEzOGNkYjc2Y2YxYWM3ZWIwZGJkNzRkMTY3ZTE1ZDcxYmEwZTg5MDAwOTNlYjU5YzJkZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.2dS48YOhoUyU6A4YoZMQZebFGzzSRpeZVQEp0kG7khs) [![Image 8: image](https://private-user-images.githubusercontent.com/2041322/330765639-675ac203-f246-41c2-b094-76318240159f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM2MDg3NTcsIm5iZiI6MTczMzYwODQ1NywicGF0aCI6Ii8yMDQxMzIyLzMzMDc2NTYzOS02NzVhYzIwMy1mMjQ2LTQxYzItYjA5NC03NjMxODI0MDE1OWYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTIwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEyMDdUMjE1NDE3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTRkNWUxNjk0MWI2MWNhZmQyZWQyZmVmZjc0MDgxYWMyMzNjZWI2YjkxMzNkMjE0MzU1MWEyMTQyNDE2ZDdiYSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.LS4sya9t_zuq_TtE1DjvZRv5DM_h5EkCUlS0ifsoWxg)](https://private-user-images.githubusercontent.com/2041322/330765639-675ac203-f246-41c2-b094-76318240159f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM2MDg3NTcsIm5iZiI6MTczMzYwODQ1NywicGF0aCI6Ii8yMDQxMzIyLzMzMDc2NTYzOS02NzVhYzIwMy1mMjQ2LTQxYzItYjA5NC03NjMxODI0MDE1OWYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTIwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEyMDdUMjE1NDE3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTRkNWUxNjk0MWI2MWNhZmQyZWQyZmVmZjc0MDgxYWMyMzNjZWI2YjkxMzNkMjE0MzU1MWEyMTQyNDE2ZDdiYSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.LS4sya9t_zuq_TtE1DjvZRv5DM_h5EkCUlS0ifsoWxg)

Updates
-------

[](https://github.com/jina-ai/reader#updates)

*   **2024-10-08**: Introduced an `adaptive crawler`. It can recursively crawl the website and extract the most relevant pages for a given webpage.
*   **2024-07-15**: To restrict the results of `s.jina.ai` to certain domain/website, you can set e.g. `site=jina.ai` in the query parameters, which enables in-site search. For more options, [try our updated live-demo](https://jina.ai/reader/#apiform).
*   **2024-07-01**: We have resolved a DDoS attack and other traffic abusing since June 27th. We also found a bug introduced on June 28th which may cause higher latency for some websites. The attack and the bug have been solved; if you have experienced high latency of r.jina.ai between June 27th-30th, it should back to normal now.
*   **2024-05-30**: Reader can now read abitrary PDF from any URL! Check out [this PDF result from NASA.gov](https://r.jina.ai/https://www.nasa.gov/wp-content/uploads/2023/01/55583main_vision_space_exploration2.pdf) vs [the original](https://www.nasa.gov/wp-content/uploads/2023/01/55583main_vision_space_exploration2.pdf).
*   **2024-05-15**: We introduced a new endpoint `s.jina.ai` that searches on the web and return top-5 results, each in a LLM-friendly format. [Read more about this new feature here](https://jina.ai/news/jina-reader-for-search-grounding-to-improve-factuality-of-llms).
*   **2024-05-08**: Image caption is off by default for better latency. To turn it on, set `x-with-generated-alt: true` in the request header.
*   **2024-05-03**: We finally resolved a DDoS attack since April 29th. Now our API is much more reliable and scalable than ever!
*   **2024-04-24**: You now have more fine-grained control over Reader API [using headers](https://github.com/jina-ai/reader#using-request-headers), e.g. forwarding cookies, using HTTP proxy.
*   **2024-04-15**: Reader now supports image reading! It captions all images at the specified URL and adds `Image [idx]: [caption]` as an alt tag (if they initially lack one). This enables downstream LLMs to interact with the images in reasoning, summarizing etc. [See example here](https://x.com/JinaAI_/status/1780094402071023926).

Usage
-----

[](https://github.com/jina-ai/reader#usage)

### Using `r.jina.ai` for single URL fetching

[](https://github.com/jina-ai/reader#using-rjinaai-for-single-url-fetching)

Simply prepend `https://r.jina.ai/` to any URL. For example, to convert the URL `https://en.wikipedia.org/wiki/Artificial_intelligence` to an LLM-friendly input, use the following URL:

[https://r.jina.ai/https://en.wikipedia.org/wiki/Artificial\_intelligence](https://r.jina.ai/https://en.wikipedia.org/wiki/Artificial_intelligence)

### [Using `r.jina.ai` for a full website fetching (Google Colab)](https://colab.research.google.com/drive/1uoBy6_7BhxqpFQ45vuhgDDDGwstaCt4P#scrollTo=5LQjzJiT9ewT)

[](https://github.com/jina-ai/reader#using-rjinaai-for-a-full-website-fetching-google-colab)

### Using `s.jina.ai` for web search

[](https://github.com/jina-ai/reader#using-sjinaai-for-web-search)

Simply prepend `https://s.jina.ai/` to your search query. Note that if you are using this in the code, make sure to encode your search query first, e.g. if your query is `Who will win 2024 US presidential election?` then your url should look like:

[https://s.jina.ai/Who%20will%20win%202024%20US%20presidential%20election%3F](https://s.jina.ai/Who%20will%20win%202024%20US%20presidential%20election%3F)

Behind the scenes, Reader searches the web, fetches the top 5 results, visits each URL, and applies `r.jina.ai` to it. This is different from many `web search function-calling` in agent/RAG frameworks, which often return only the title, URL, and description provided by the search engine API. If you want to read one result more deeply, you have to fetch the content yourself from that URL. With Reader, `http://s.jina.ai` automatically fetches the content from the top 5 search result URLs for you (reusing the tech stack behind `http://r.jina.ai`). This means you don't have to handle browser rendering, blocking, or any issues related to JavaScript and CSS yourself.

### Using `s.jina.ai` for in-site search

[](https://github.com/jina-ai/reader#using-sjinaai-for-in-site-search)

Simply specify `site` in the query parameters such as:

curl 'https://s.jina.ai/When%20was%20Jina%20AI%20founded%3F?site=jina.ai&site=github.com'

### [Interactive Code Snippet Builder](https://jina.ai/reader#apiform)

[](https://github.com/jina-ai/reader#interactive-code-snippet-builder)

We highly recommend using the code builder to explore different parameter combinations of the Reader API.

[![Image 9: image](https://private-user-images.githubusercontent.com/2041322/330768792-a490fd3a-1c4c-4a3f-a95a-c481c2a8cc8f.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM2MDg3NTcsIm5iZiI6MTczMzYwODQ1NywicGF0aCI6Ii8yMDQxMzIyLzMzMDc2ODc5Mi1hNDkwZmQzYS0xYzRjLTRhM2YtYTk1YS1jNDgxYzJhOGNjOGYuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTIwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEyMDdUMjE1NDE3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YjYzNzc0M2FhM2Q0ZGRkMzE2MTZiN2IxNGYyYmNjMWI4OTY3NzRlN2IwOTU2NGU5NGQyYmUxZjQzZTI2NzQ3NCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.mQa7G_B-85KHdaVmzC9zWYfjEzKxqcBMkicZNbD9qnw)](https://jina.ai/reader#apiform)

### Using request headers

[](https://github.com/jina-ai/reader#using-request-headers)

As you have already seen above, one can control the behavior of the Reader API using request headers. Here is a complete list of supported headers.

*   You can enable the image caption feature via the `x-with-generated-alt: true` header.
*   You can ask the Reader API to forward cookies settings via the `x-set-cookie` header.
    *   Note that requests with cookies will not be cached.
*   You can bypass `readability` filtering via the `x-respond-with` header, specifically:
    *   `x-respond-with: markdown` returns markdown _without_ going through `reability`
    *   `x-respond-with: html` returns `documentElement.outerHTML`
    *   `x-respond-with: text` returns `document.body.innerText`
    *   `x-respond-with: screenshot` returns the URL of the webpage's screenshot
*   You can specify a proxy server via the `x-proxy-url` header.
*   You can customize cache tolerance via the `x-cache-tolerance` header (integer in seconds).
*   You can bypass the cached page (lifetime 3600s) via the `x-no-cache: true` header (equivalent of `x-cache-tolerance: 0`).
*   If you already know the HTML structure of your target page, you may specify `x-target-selector` or `x-wait-for-selector` to direct the Reader API to focus on a specific part of the page.
    *   By setting `x-target-selector` header to a CSS selector, the Reader API return the content within the matched element, instead of the full HTML. Setting this header is useful when the automatic content extraction fails to capture the desired content and you can manually select the correct target.
    *   By setting `x-wait-for-selector` header to a CSS selector, the Reader API will wait until the matched element is rendered before returning the content. If you already specified `x-wait-for-selector`, this header can be omitted if you plan to wait for the same element.

### Using `r.jina.ai` for single page application (SPA) fetching

[](https://github.com/jina-ai/reader#using-rjinaai-for-single-page-application-spa-fetching)

Many websites nowadays rely on JavaScript frameworks and client-side rendering. Usually known as Single Page Application (SPA). Thanks to [Puppeteer](https://github.com/puppeteer/puppeteer) and headless Chrome browser, Reader natively supports fetching these websites. However, due to specific approach some SPA are developed, there may be some extra precautions to take.

#### SPAs with hash-based routing

[](https://github.com/jina-ai/reader#spas-with-hash-based-routing)

By definition of the web standards, content come after `#` in a URL is not sent to the server. To mitigate this issue, use `POST` method with `url` parameter in body.

curl -X POST 'https://r.jina.ai/' -d 'url=https://example.com/#/route' 

#### SPAs with preloading contents

[](https://github.com/jina-ai/reader#spas-with-preloading-contents)

Some SPAs, or even some websites that are not strictly SPAs, may show preload contents before later loading the main content dynamically. In this case, Reader may be capturing the preload content instead of the main content. To mitigate this issue, here are some possible solutions:

##### Specifying `x-timeout`

[](https://github.com/jina-ai/reader#specifying-x-timeout)

When timeout is explicitly specified, Reader will not attempt to return early and will wait for network idle until the timeout is reached. This is useful when the target website will eventually come to a network idle.

curl 'https://example.com/' -H 'x-timeout: 30'

##### Specifying `x-wait-for-selector`

[](https://github.com/jina-ai/reader#specifying-x-wait-for-selector)

When wait-for-selector is explicitly specified, Reader will wait for the appearance of the specified CSS selector until timeout is reached. This is useful when you know exactly what element to wait for.

curl 'https://example.com/' -H 'x-wait-for-selector: #content'

### Streaming mode

[](https://github.com/jina-ai/reader#streaming-mode)

Streaming mode is useful when you find that the standard mode provides an incomplete result. This is because the Reader will wait a bit longer until the page is _stablely_ rendered. Use the accept-header to toggle the streaming mode:

curl -H "Accept: text/event-stream" https://r.jina.ai/https://en.m.wikipedia.org/wiki/Main\_Page

The data comes in a stream; each subsequent chunk contains more complete information. **The last chunk should provide the most complete and final result.** If you come from LLMs, please note that it is a different behavior than the LLMs' text-generation streaming.

For example, compare these two curl commands below. You can see streaming one gives you complete information at last, whereas standard mode does not. This is because the content loading on this particular site is triggered by some js _after_ the page is fully loaded, and standard mode returns the page "too soon".

curl -H 'x-no-cache: true' https://access.redhat.com/security/cve/CVE-2023-45853
curl -H "Accept: text/event-stream" -H 'x-no-cache: true' https://r.jina.ai/https://access.redhat.com/security/cve/CVE-2023-45853

> Note: `-H 'x-no-cache: true'` is used only for demonstration purposes to bypass the cache.

Streaming mode is also useful if your downstream LLM/agent system requires immediate content delivery or needs to process data in chunks to interleave I/O and LLM processing times. This allows for quicker access and more efficient data handling:

```
Reader API:  streamContent1 ----> streamContent2 ----> streamContent3 ---> ... 
                          |                    |                     |
                          v                    |                     |
Your LLM:                 LLM(streamContent1)  |                     |
                                               v                     |
                                               LLM(streamContent2)   |
                                                                     v
                                                                     LLM(streamContent3)
```

Note that in terms of completeness: `... > streamContent3 > streamContent2 > streamContent1`, each subsequent chunk contains more complete information.

### JSON mode

[](https://github.com/jina-ai/reader#json-mode)

This is still very early and the result is not really a "useful" JSON. It contains three fields `url`, `title` and `content` only. Nonetheless, you can use accept-header to control the output format:

curl -H "Accept: application/json" https://r.jina.ai/https://en.m.wikipedia.org/wiki/Main\_Page

JSON mode is probably more useful in `s.jina.ai` than `r.jina.ai`. For `s.jina.ai` with JSON mode, it returns 5 results in a list, each in the structure of `{'title', 'content', 'url'}`.

### Generated alt

[](https://github.com/jina-ai/reader#generated-alt)

All images in that page that lack `alt` tag can be auto-captioned by a VLM (vision langauge model) and formatted as `!(Image [idx]: [VLM_caption])[img_URL]`. This should give your downstream text-only LLM _just enough_ hints to include those images into reasoning, selecting, and summarization. Use the x-with-generated-alt header to toggle the streaming mode:

curl -H "X-With-Generated-Alt: true" https://r.jina.ai/https://en.m.wikipedia.org/wiki/Main\_Page

Install
-------

[](https://github.com/jina-ai/reader#install)

You will need the following tools to run the project:

*   Node v18 (The build fails for Node version \>18)
*   Firebase CLI (`npm install -g firebase-tools`)

For backend, go to the `backend/functions` directory and install the npm dependencies.

git clone git@github.com:jina-ai/reader.git
cd backend/functions
npm install

What is `thinapps-shared` submodule?
------------------------------------

[](https://github.com/jina-ai/reader#what-is-thinapps-shared-submodule)

You might notice a reference to `thinapps-shared` submodule, an internal package we use to share code across our products. While it’s not open-sourced and isn't integral to the Reader's functions, it mainly helps with decorators, logging, secrets management, etc. Feel free to ignore it for now.

That said, this is _the single codebase_ behind `https://r.jina.ai`, so everytime we commit here, we will deploy the new version to the `https://r.jina.ai`.

Having trouble on some websites?
--------------------------------

[](https://github.com/jina-ai/reader#having-trouble-on-some-websites)

Please raise an issue with the URL you are having trouble with. We will look into it and try to fix it.

License
-------

[](https://github.com/jina-ai/reader#license)

Reader is backed by [Jina AI](https://jina.ai/) and licensed under [Apache-2.0](https://github.com/jina-ai/reader/blob/main/LICENSE).