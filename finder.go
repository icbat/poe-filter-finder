package main

import "fmt"
import "os"

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
	fmt.Println("Downloading filter file to temp directory: " + os.TempDir())
	filterURL := "https://raw.githubusercontent.com/icbat/LootFilter/master/ThioleLootFilter"
	fmt.Println("Grabbing filter file from: " + filterURL)
	downloadTo(filterURL, os.TempDir())
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

func downloadTo(remotePath string, targetDirectory string) {
	tempFile, err := os.Create(os.TempDir() + "/poe-filter-file.txt")
	if err != nil {
		return
	}
	defer tempFile.Close()

}
