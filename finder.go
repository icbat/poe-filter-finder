package main

import (
	"fmt"
	"io/ioutil"
)
import "os"
import "net/http"

func main() {
	fmt.Println("Checking environment")
	basePath := resolveEnvVariables()
	if basePath == "" {
		fmt.Println(" -- Couldn't resolve environment variables!")
		return
	}
	fmt.Println("Found base path of: " + basePath)

	fmt.Println("Verifying directories")
	path := basePath + "/Documents/My Games/Path of Exile"
	if !pathExists(path) {
		fmt.Println(" -- Couldn't find a folder at " + path)
		return
	}
	fmt.Println("Found PoE folder at: " + path)

	fmt.Println("Reticulating splines")
	filterName := "ThioleLootFilter"
	filterURL := "https://raw.githubusercontent.com/icbat/LootFilter/master/" + filterName
	fmt.Println("Grabbing filter file from: " + filterURL)
	downloadTo(filterURL, path+"/"+filterName)
}

func resolveEnvVariables() string {
	return os.Getenv("UserProfile")
}

func pathExists(path string) bool {
	_, err := os.Stat(path)
	if err == nil {
		return true
	}
	fmt.Println(err)
	return false
}

func downloadTo(url string, targetFile string) {
	response, err := http.Get(url)
	if err != nil {

	}
	defer response.Body.Close()

	bytes, err := ioutil.ReadAll(response.Body)

	ioutil.WriteFile(targetFile, bytes, 0644)
}
