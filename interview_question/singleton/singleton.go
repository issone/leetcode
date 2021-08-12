package main

import (
	"fmt"
	"sync"
)

type Instance struct {
	name string
}


var once sync.Once
var lock sync.Mutex

// 私有的实例指针
var instance *Instance

// sync.Once版本
func GetInstance() *Instance {
	once.Do(func() {
		instance = &Instance{}	// new(Instance)
	})
	return instance
}

// 带检查锁的单例模式

func GetInstance2() *Instance {

	if instance == nil {
		// 注意加锁的位置，不要一进来就加锁，否则已生成实例后还要加锁，浪费资源
		lock.Lock()
		defer lock.Unlock()
		if instance == nil {
			instance = &Instance{}
		}
	}
	return instance

}

func main() {
	a:=GetInstance2()
	b:=GetInstance2()
	fmt.Printf("%p,%p",a,b)

}