# SYSTEM CHECK
> My friend David, who is a manager at company XYX, handles all types of calculations and user data on his exceptionally fast computer. Due to its speed and the abundance of data it contains, his computer became a common target for Black hat hackers seeking to compromise high-performance systems with valuable information. As a result, hackers targeted David's computer. However, it wasn't just one hacker involved; there was another hacker aiming to gain physical access to the computer using a rubber ducky.

> Both hackers managed to successfully breach the computer's security and install their own software as desired. Upon starting his computer, David noticed TWO unusual pop-ups and experienced a significant decrease in system performance. Worried about the situation, he checked the task manager and observed abnormal resource usage.

> In response to David's concern, he informed me, and I conducted some forensic investigation. David provided me with the .ova file to analyze further. With this information, I will thoroughly research the Windows system, identify the extent of the compromise, and recommend appropriate remediation steps to alleviate the effects of the hacking incident. Rest assured, I will do my best to assist my friend David and help him restore his computer's security and normal functionality.

> As a White hat hacker Can you please help me to find out some thing?

> Config Note: {Uncheck additional options: Import Hard drives as VDI} And {Don't Press any key when It need boot from CD AND DVD}

> Note:When you find any PATH.I intentionally changed the executable file name with .extention or only folder path.

> When Last system audit policy was changed?

> Flag Format:BDSEC{MM/DD/YEAR_Hour:Minute:Second_Am/PM}

> Example: BDSEC{01/01/2001_01:01:01_PM}

## About the Challenge
We need to find when the system audit policy was changed

## How to Solve?
Open `Windows event` and then find a Windows log event with ID `4719`

![flag](images/flag.png)

And then find the latest event

```
BDSEC{07/20/2023_07:12:17_AM}
```