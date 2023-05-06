# Extract Service 1
> We have released a summary service for document files! Please feel free to use the sample document file in the "sample" folder of the distribution file for trial purposes.

> The secret information is written in the /flag file on the server, but it should be safe, right...? Let's see what kind of HTTP request is sent!

## About the Challenge
We have been given a website and a source code (You can download the file [here](web-extract1.zip)). This website can read the docx, xlsx, and pptx files that we have uploaded

![preview](images/preview.png)

## How to Solve?
If you check the source code especially on `main.go` file, there is a function called `ExtractContent` where this function can read any file by using `os.ReadFile` function

```go
func ExtractContent(baseDir, extractTarget string) (string, error) {
	raw, err := os.ReadFile(filepath.Join(baseDir, extractTarget))
	if err != nil {
		return "", err
	}

	removeXmlTag := regexp.MustCompile("<.*?>")
	resultXmlTagRemoved := removeXmlTag.ReplaceAllString(string(raw), "")
	removeNewLine := regexp.MustCompile(`\r?\n`)
	resultNewLineRemoved := removeNewLine.ReplaceAllString(resultXmlTagRemoved, "")
	return resultNewLineRemoved, nil
}
```

And because of there is no filter in the `extractTarget` variable (You can check this in line 38 - 44)

```go
		extractTarget := c.PostForm("target")
		if extractTarget == "" {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : target is required",
			})
			return
		}
```

This website is vulnerable to directory traversal attack. To obtain the flag we need to change the value of the `target` parameter to `../../../../../../flag`

![flag](images/flag.png)

```
FLAG{ex7r4c7_1s_br0k3n_by_b4d_p4r4m3t3rs}
```