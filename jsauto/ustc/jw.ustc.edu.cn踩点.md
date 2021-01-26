
## [ustc教务系统](jw.ustc.edu.cn)自动选课

1.0.0.20210126


html没用，全是登录前的那个界面

确认选课公告：
document.querySelector("#modal-info-content > div.modal.fade.alter-modal.in > div > div > div.modal-footer > button.btn.btn-default.close-modal.bulletin-prompt").click()

关闭(选课失败)：
document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div > div.modal-footer > button.btn.btn-default.close-modal").click()

选课：
document.querySelector("#DataTables_Table_0 > tbody > tr:nth-child(4) > td.sorting_1 > button").click()

选课结果(成功或失败)对话框：
document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div")

隐藏该对话框(用了会卡住，因为该对话框未关闭)：
document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div").setAttribute('hidden',true)

确认退课：
document.querySelector("body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-primary").click()

取消退课：
document.querySelector("body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-default").click()

选课结果标题：
document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div > div.modal-header > h4")

依据课程名称选课
document.querySelector("#DataTables_Table_0 > tbody > tr:nth-child(3) > td:nth-child(4) > span").parentElement.parentElement.firstElementChild.firstElementChild.click()



循环选课示例：
```javascript

var interval1=setInterval(() => {
    document.querySelector("#DataTables_Table_0 > tbody > tr:nth-child(1) > td.sorting_1 > button").click()
    // debugger

    setTimeout(() => {
        close_result()
    }, 1500);//1.5秒后close选课结果
}, 2000);//clearInterval(interval1)可以停下来




function close_result(){
    waiting = document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div > div.modal-header > h4")

    while (waiting) {
        close_result_btn = document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div > div.modal-footer > button.btn.btn-default.close-modal")
        if (close_result_btn) {
            close_result_btn.click()
        }

        waiting = document.querySelector("#modal-info-content > div.modal.fade.add-response.in > div > div > div.modal-header > h4")
    }
}

```

输入`clearInterval(interval1)`以终止程序



