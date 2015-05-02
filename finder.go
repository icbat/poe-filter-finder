package main

import "fmt"
import "os"

func main() {
	fmt.Println("Checking environment")
	basePath := resolveenvironment()
	if basePath == "" {
		fmt.Println(" -- Couldn't resolve environment variables!")
		return
	}
	fmt.Println("Found base path of: " + basePath)

	fmt.Println("Verifying directories")
	fmt.Println("Reticulating splines")
	fmt.Println("Downloading filter file")
}

func resolveenvironment() string {
	return os.Getenv("UserProfile")
}
