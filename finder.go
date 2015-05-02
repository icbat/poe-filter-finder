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
	fmt.Println("Targeting: " + path)

	fmt.Println("Reticulating splines")
	fmt.Println("Downloading filter file to temp directory: " + os.TempDir())
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
