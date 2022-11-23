![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/cloudshell_logo.png)

# **Cisco TRex Shells**  

Release date: March 2018

Shell version: 3.0.0

Document version: 1.1

# In This Guide

* [Overview](#overview)
* [Downloading the Shell](#downloading-the-shell)
* [Importing and Configuring the Shell](#importing-and-configuring-the-shell)
* [Updating Python Dependencies for Shells](#updating-python-dependencies-for-shells)
* [Typical Workflows](#typical-workflows)
* [References](#references)
* [Release Notes](#release-notes)


# Overview
A shell integrates a device model, application or other technology with CloudShell. A shell consists of a data model that defines how the device and its properties are modeled in CloudShell, along with automation that enables interaction with the device via CloudShell.

**Note:** We recommend using a 2nd gen shell where possible. Using a 1st gen shell may limit some shell management capabilities. For more information, see [Shell Overview – “Our Shell”](http://help.quali.com/Online%20Help/8.3/Portal/Content/CSP/LAB-MNG/Shells.htm?Highlight=shell%20overview). 

### Traffic Generator Shells
CloudShell's traffic generator shells enable you to conduct traffic test activities on Devices Under Test (DUT) or Systems Under Test (SUT) from a sandbox. In CloudShell, a traffic generator is typically modeled using a chassis resource, which represents the traffic generator device and ports, and a controller service that runs the chassis commands, such as Load Configuration File, Start Traffic and Get Statistics. Chassis and controllers are modeled by different shells, allowing you to accurately model your real-life architecture. For example, scenarios where the chassis and controller are located on different machines.

For additional information on traffic generator shell architecture, and setting up and using a traffic generator in CloudShell, see the [Traffic Generators Overiew](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Trffc-Gens.htm?Highlight=traffic%20generator%20overview) online help topic.

### **Cisco TRex Shells**

To model a **Cisco TRex** device in CloudShell, use one of the following options for either a standard or virtual configuration:

**Standard Option**

▪ [Cisco TRex Chassis 2 Gen Shell](https://community.quali.com/repos/3412/cloudshell-trex-chassis-2-gen-shell), which provides data model and autoload functionality to model and load the Cisco TRex Chassis to resource management.

▪ [Cisco TRex Controller 1G Shell (service)](https://community.quali.com/repos/3410/cloudshell-trex-controller-shell), which provides functionality to load test configuration, run tests, get test results, etc.

**Virtual Option**

▪ [CloudShell TRex Virtual Traffic Generator 1G Shell](https://community.quali.com/repos/3409/cloudshell-trex-virtual-traffic-generator-shell), which creates a CloudShell TRex virtual traffic generator shell. Using this shell, you can create an App that, once deployed in a sandbox, will spin up a VM that models a Cisco TRex traffic generator. 

• [Cisco TRex Controller 1G Shell (service)](https://community.quali.com/repos/3410/cloudshell-trex-controller-shell), which provides functionality to load test configuration, run tests, get tests results, etc.

For more information on the **Cisco TRex** traffic generators, see the official **Cisco TRex** product documentation.

### Standard version

For detailed information about the shell’s structure and attributes, see the [**Traffic Shell Standard**](https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/traffic_standard.md) in GitHub.

### Requirements

Release: **Cisco TRex Shells**

▪ CloudShell version: 8.2 and above

▪ Cisco TRex versions: 2.35 and above

▪ Cisco TRex server versions: 2.35 and above

**Note:** If your CloudShell version does not support this shell, you should consider upgrading to a later version of CloudShell or contact customer support.

### Data Model

The shell data models include all shell metadata, families, and attributes.

#### **CloudShell TRex Chassis 2G Families and Models**

The chassis families and models are listed in the following table:

|Family|Model|Description|
|:---|:---|:---|
|Traffic Generator Chassis|TRex Chassis|TRex Chassis|
|Port|Generic Traffic Generator Port|Generic Traffic Generator Port|

#### **CloudShell TRex Virtual Traffic Generator 1G Families and Models**

The virtual traffic generator families and models are listed in the following table:

|Family|Model|Description|
|:---|:---|:---|
|Virtual Traffic Generator Chassis|Cisco TRex Chassis|Virtual TRex Chassis|
|Port|TRex Virtual Port|Cisco TRex virtual port|

#### **Attributes**

**Cloudshell TRex Chassis 2G Attributes**

The chassis attribute names and types are listed in the following table:

|Attribute|Type|Description|
|:---|:---|:---|
|Logical Name|String|Port's logical name in the test configuration. If left empty, automatic allocation will be applied.|
|Media Type|String|Interface media type.<br> Possible values are: **Fiber** and/or **Copper** (comma-separated).|
|Model Name|String|Device model. This information is typically used for abstract resource filtering.|
|Power Management|Boolean|Used by the power management orchestration, if enabled, to determine whether to automatically manage the device power status. Enabled by default.|
|Supported Speeds|String|Speed supported by the interface (comma-separated).|
|Server Description|String|Full description of the server. Usually includes the OS, exact firmware version and additional characteristics of the device.
|Version|String|Firmware version of the resource.|
|Vendor|String|Name of the device manufacturer.|

**CloudShell TRex Virtual Traffic Generator Attributes**

The CloudShell TRex virtual traffic generator attribute names and types are listed in the following table:

|Attribute|Type|Default value|Description|
|:---|:---|:---|:---|
|Logical Name|String||Virtual port's logical name in the test configuration. If left empty, automatic allocation will be applied.|
|Requested vNIC Name|String||VNic to be associated with the vPort.|
|Update TRex|Boolean|False|If set to **True**, the shell will automatically try to install/update TRex.|
|TRex Package URL|String|http://trex-tgn.cisco.com/trex/release/latest |Path to the TRex package.<br>The path should include the protocol type, for example *http://trex-tgn.cisco.com/trex/release/latest*.|
|TRex Server Config|String||Path to the TRex server configuration.|

**CloudShell TRex Controller Attributes**

The Cloudshell TRex controller attribute names and types are listed in the following table:

|Attribute|Type|Description|
|:---|:---|:---|
|Test Files Location|String|Location for the test related files.|

### Automation
This section describes the automation (driver) associated with the data model. The shell’s driver is provided as part of the shell package. There are two types of automation processes, Autoload and Resource.  Autoload is executed when creating the resource in the **Inventory** dashboard, while resource commands are run in the sandbox.

For Traffic Generator shells, commands are configured and executed from the controller service in the sandbox, with the exception of the Autoload command, which is executed when creating the resource. 

The following table describes the process that occurrs during Autoload for the different TRex shells:

|Shell|Description|
|:-----|:-----|
|CloudShell TRex Chassis 2G|Discovers the chassis, its hierarchy and attributes when creating the resource. The command can be rerun in the Inventory dashboard and not in the sandbox, as for other commands.|
|Cisco TRex Controller 1G|Discovers the chassis, its hierarchy and attributes when creating the resource. The command is executed when creating the resource.|
|CloudShell TRex Virtual Traffic Generator 1G|Creates the device structure, its hierarchy and attributes when deploying the App.|

**CloudShell TRex Controller 1G Shell**

**Note**: For detailed information on running a traffic test in CloudShell, see [Traffic Generators Overview](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Trffc-Gens.htm?Highlight=traffic%20generators%20overview).

|Command|Description|
|:-----|:-----|
|Upload Server Configuration|Uploads the current TRex server configuration file to the remote FTP/TFTP server.|
|Download Server Configuration|Downloads the configuration file from the remote FTP/TFTP server and sets it as the TRex server configuration file.|
|Load Configuration|Loads the configuration file (configured by your admin).<br>The load configuration file includes the settings to run the traffic test, for example, packet size, number of packets to send in parallel, interval at which to send packet batches, etc. The file also reserves the necessary ports.<br>The load configuration file must be accessible from the Execution Server, see [Traffic Generators Overview](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Trffc-Gens.htm?Highlight=traffic%20Generators%20overview).|
|Start Traffic|Starts a test to generate and send traffic from the traffic generator.|
|Stop Traffic|Stops running a test to stop sending traffic from the traffic generator.|
|Get Result|Gets the test result file and attaches it to the sandbox.|
|Get Test File|Downloads the test file to the location specified in the **Test Files Location** attribute, defined when you added the service to your blueprint.


# Downloading the Shells
The **Cisco TRex** shells are available from the [Quali Community Integrations](https://community.quali.com/integrations) page. 

Download the files into a temporary location on your local machine. 

The shells comprise:

|File name|Description|
|:---|:---|
|cisco-virtual-trex.zip|CloudShell TRex virtual traffic generator shell package|
|virtual-trex-offline-packages-1.0.0.zip|CloudShell TRex virtual traffic generator shell Python dependencies (for offline deployments only)|
|trex_controller_shell.zip|CloudShell TRex controller shell package|
|trex_controller-offline-dependencies-1.0.0.zip|CloudShell TRex controller shell Python dependencies (for offline deployments only)|
|TRexChassisShell2G.zip|CloudShell TRex chassis 2G shell package|
|trex_chassis_2g_offline_dependencies-1.0.0.zip|CloudShell TRex chassis 2G shell Python dependencies (for offline deployments only|
|cloudshell-tg-trex-1.0.0.zip|Part of the offline deployments package|

# Importing and Configuring the Shells
This section describes how to import the **Cisco TRex** shells and configure and modify the shell devices.

### Importing the shells into CloudShell

**To import the CloudShell TRex Controller and the CloudShell TRex Virtual Traffic Generator 1G shells into CloudShell**

  1. Make sure you have the shell’s zip package. If not, download the shell from the [Quali Community's Integrations](https://community.quali.com/integrations) page.
  
  2. Backup your database.
  
  3. Log in to CloudShell Portal as administrator and access the relevant domain.
  
  4. In the user menu select **Import Package**.
  
     ![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/import_package.png)
     
  5. Browse to the location of the downloaded shell file, select the relevant *.zip* file and Click **Open**. Alternatively, drag the shell’s .zip file into CloudShell Portal.
  
  6. Import the second shell by repeating steps 4 and 5.<br><br>The CloudShell TRex controller shell is displayed in the **App/Service>Applications** section of your blueprint, and can be used to run custom code and automation processes in the sandbox. For more information, see [Services Overview](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Services.htm?Highlight=services).<br><br>You can now use the CloudShell TRex virtual traffic generator shell to create Apps that, once deployed in a sandbox, will spin up VMs that model a Cisco TRex traffic generator. See [Configuring a new App](#configuring-a-new-app). For more information, see [Apps Overview](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Apps.htm?Highlight=applications). 


**To import the CloudShell TRex Chassis 2G shell into CloudShell**

  1. Make sure you have the shell’s zip package. If not, download the shell from the [Quali Community's Integrations](https://community.quali.com/integrations) page.
  
  2. In CloudShell Portal, as Global administrator, open the **Manage – Shells** page.
  
  3. Click **Import**.
  
  4. In the dialog box, navigate to the shell's zip package, select it and click **Open**. <br><br>The shell is displayed in the **Shells** page and can be used by domain administrators in all CloudShell domains to create new inventory resources, as explained in [Adding Inventory Resources](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Add-Rsrc-Tmplt.htm?Highlight=adding%20inventory%20resources). 
  
  5. Download the Cisco TRex Controller 1G shell, if you have not already done so. See [To import the CloudShell TRex Controller](#to-import-the-cloudshell-trex-controller-and-the-cloudchell-trex-virtual-traffic-generator-1g-shells-into-cloudshell)

### Offline installation of a shell

**Note:** Offline installation instructions are relevant only if CloudShell Execution Server has no access to PyPi. You can skip this section if your execution server has access to PyPi. For additional information, see the online help topic on offline dependencies.

In offline mode, import the shell into CloudShell and place any dependencies in the appropriate dependencies folder. The dependencies folder may differ, depending on the CloudShell version you are using:

* For CloudShell version 8.3 and above, see [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository).

* For CloudShell version 8.2, perform the appropriate procedure: [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository) or [Setting the python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

### Adding shell and script packages to the local PyPi Server repository
If your Quali Server and/or execution servers work offline, you will need to copy all required Python packages, including the out-of-the-box ones, to the PyPi Server's repository on the Quali Server computer (by default *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Config\Pypi Server Repository*).

For more information, see [Configuring CloudShell to Execute Python Commands in Offline Mode](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=Configuring%20CloudShell%20to%20Execute%20Python%20Commands%20in%20Offline%20Mode).

**To add Python packages to the local PyPi Server repository:**
  1. If you haven't created and configured the local PyPi Server repository to work with the execution server, perform the steps in [Add Python packages to the local PyPi Server repository (offline mode)](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=offline%20dependencies#Add). 
  
  2. For each shell or script you add into CloudShell, do one of the following (from an online computer):
      * Connect to the Internet and download each dependency specified in the *requirements.txt* file with the following command: 
`pip download -r requirements.txt`. 
     The shell or script's requirements are downloaded as zip files.

      * In the [Quali Community's Integrations](https://community.quali.com/integrations) page, locate the shell and click the shell's **Download** link. In the page that is displayed, from the Downloads area, extract the dependencies package zip file.

3. Place these zip files in the local PyPi Server repository.
 
### Setting the python PythonOfflineRepositoryPath configuration key
Before PyPi Server was introduced as CloudShell’s python package management mechanism, the `PythonOfflineRepositoryPath` key was used to set the default offline package repository on the Quali Server machine, and could be used on specific Execution Server machines to set a different folder. 

**To set the offline python repository:**
1. Download the relevant *offline_dependencies.zip* file, see [Downloading the Shell](#downloading-the-shell):

	• virtual-trex-offline-packages-1.0.0.zip
	
	• trex_controller-offline-dependencies-1.0.0.zip
	
	• trex_chassis_2g_offline_dependencies-1.0.0.zip
	
	• cloudshell-tg-trex-1.0.0.zip

2. Unzip it to a local repository. Make sure the execution server has access to this folder. 

3.  On the Quali Server machine, in the *~\CloudShell\Server\customer.config* file, add the following key to specify the path to the default python package folder (for all Execution Servers):  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

4. If you want to override the default folder for a specific Execution Server, on the Execution Server machine, in the *~TestShell\Execution Server\customer.config* file, add the following key:  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

5. Restart the Execution Server.

### Configuring a new resource
This section explains how to create a new resource from the CloudShell TRex Chassis 2G shell.

In CloudShell, the component that models the device is called a resource. It is based on the shell that models the device and allows the CloudShell user and API to remotely control the device from CloudShell.

You can also modify existing resources, see [Managing Resources in the Inventory](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Mng-Rsrc-in-Invnt.htm?Highlight=managing%20resources).

**To create a resource for the device:**
  1. In the CloudShell Portal, in the **Inventory** dashboard, click **Add New**. 
     ![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/create_a_resource_device.png)
     
  2. From the list, select **Cisco TRex Chassis**.
  
  3. Enter the **Name** and **IP address** of the **Cisco TRex Chassis**.
  
  4. Click **Create**.
  
  5. In the **Resource** dialog box, enter the device's settings. For details, see [Device Name Attributes](#device-name-attributes). 
  
  6. Click **Continue**. <br><br>CloudShell validates the device’s settings and updates the new resource with the device’s structure.
  
### Configuring the setup script
This section explains how to modify the setup script to work with the **CloudShell TRex Virtual Traffic Generator** shell.

**To modify the setup script:**
1. Log in to CloudShell Portal as administrator of the relevant domain.

2. Go to the **Manage** dashboard and click **Scripts>Blueprint**.

3. Download the current setup script.

4. Browse to the location of the downloaded file. 

5. Add *cloudshell-orch-trex>=1.0.0,<1.1.0* into the *requirements.txt* file.

6. Add the following code in the *_main_.py* file:

	`from cloudshell.workflow.orchestration.setup.trex.configuration_commands import configure_virtual_chassis, execute_autoload_on_trexsandbox.workflow.add_to_configuration(function=configure_virtual_chassis, components=sandbox.components.apps)
sandbox.workflow.on_configuration_ended(function=execute_autoload_on_trex, components=sandbox.components.apps))`

7. Update the setup script in CloudShell.

# Updating Python Dependencies for Shells
This section explains how to update your Python dependencies folder. This is required when you upgrade a shell that uses new/updated dependencies. It applies to both online and offline dependencies.

### Updating offline Python dependencies
**To update offline Python dependencies:**
1. Download the latest Python dependencies package zip file locally.

2. Extract the zip file to the suitable offline package folder(s). 

3. Terminate the shell’s instance, as explained [here](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/MNG/Mng-Exctn-Srv-Exct.htm#Terminat).

### Updating online Python dependencies
In online mode, the execution server automatically downloads and extracts the appropriate dependencies file to the online Python dependencies repository every time a new instance of the driver or script is created.

**To update online Python dependencies:**
* If there is a live instance of the shell's driver or script, terminate the shell’s instance, as explained [here](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/MNG/Mng-Exctn-Srv-Exct.htm#Terminat). If an instance does not exist, the execution server will download the Python dependencies the next time a command of the driver or script runs.

# Typical Workflows 

**Workflow 1** - *Creating a new blueprint* 

1. Log in to CloudShell Portal and create a new blueprint (**Blueprint Catalog>Create Blueprint**).

2. Give the blueprint a name.
   
3. Add resources and services to the blueprint. 
  	1. Click the **Resources** tab from the toolbar and add the **TRex Chassis** resource and all required ports.
   	2. Click the **App/Services** tab from the toolbar and add the **Cisco TRex Controller** service.
   	3. Specify the **Test Files Location**, where test files will be downloaded.

**Workflow 2** - *Getting the TRex server configuration file* 

1. Log in to CloudShell Portal and reserve the blueprint.

2. Hover over the **TRex Controller** resource and select the **Commands** button from the context menu.

3. Run the **Upload Server Configuration** command and specify the input value as follows: 

	* **URL Path (String)**: Enter the full path of the FTP/TFTP in which the current TRex server configuration file will be saved.
	
4. Run the **Upload Server Configuration** command. 

3. Enter the FTP/TFTP server folder and verify that the TRex server configuration was copied successfully.

**Workflow 3** - *Setting the TRex server configuration file* 

1. Log in to CloudShell Portal and reserve the blueprint.

2. Hover over the **TRex Controller** resource and select the **Commands** button from the context menu.

4. Run the **Download Server Configuration** command and specify the input value as follows: 

	* **URL Path (String)**: Enter the full path to the TRex server configuration file, including the configuration file name.

3. Run the **Download Server Configuration** command.
	
**Workflow 4** - *Loading the TRex test configuration file* 

1. Log in to CloudShell Portal and reserve the blueprint.

2. Hover over the **TRex Controller** resource and select the **Commands** button from the context menu.

3. Run the **Load Test Configuration** command and specify the input value as follows: 

	* **URL Path (String)**: Enter the path to the TRex test configuration file, including the configuration file name.<br> The path can be accessed in two ways:<br>• Path to the configuration file on the FTP/TFTP server<br>• Relative path to the configuration file under **Test Files Location**.
	
4. Run the **Load Test Configuration** command.
	
**Workflow 5** - *Running a test* 

1. Reserve a blueprint that is configured to run traffic tests, like the one configured in Workflow 1.

2. Run the **Start Test** command.
	1. Hover over the **TRex Controller** resource and select the **Commands** button from the context menu.
	2. Run the **Start Traffic** command and specify the required parameters:
	
		• **Block**: Set to **True** to execute the command when the TRex state changes from **Starting** to either **Idle** or **Running**.
		
		• **Timeout**: Maximum time (in seconds) to wait in the **Block** state until the TRex state changes from **Starting** to either **Idle** or **Running**.
		
		• **Latency**: Latency packets rate (Hz).
	3. Execute the **Start Traffic** command.

3. Run **Stop Test**.
	1. Hover over the **TRex Controller** resource and select the **Commands** button from the context menu.
	2. Run the **Stop Traffic** command and enter the **Run** menu.
	3. Specify the following parameter, as required:
	
		• **Force**: Forces the TRex process (if it exists) to stop running on the server.
	4. Run the **Stop Traffic** command.
	
4. Run **Get Result** command.
	
# References
To download and share integrations, see [Quali Community's Integrations](https://community.quali.com/integrations). 

For instructional training and documentation, see [Quali University](https://www.quali.com/university/).

To suggest an idea for the product, see [Quali's Idea box](https://community.quali.com/ideabox). 

To connect with Quali users and experts from around the world, ask questions and discuss issues, see [Quali's Community forums](https://community.quali.com/forums). 

To use traffic generator ports as abstract resources, see [CloudShell's Online Help](https://help.quali.com/Online%20Help/9.1/Portal/Content/CSP/LAB-MNG/Traffic-Gens-Abst.htm?Highlight=traffic%20generator).

# Release Notes 

### What's New

For release updates, see the shell's GitHub release pages as follows:

▪ [Cisco TRex Chassis 2 Gen Shell release page](https://github.com/QualiSystems/Ixia-Chassis-Shell-2G/releases)

▪ [Cisco TRex Controller 1G Shell release page](https://github.com/QualiSystems/TRex-Controller-Shell/releases)

▪ [CloudShell TRex Virtual Traffic Generator 1G Shell release page](https://github.com/QualiSystems/cloudshell-tg-virtual-trex/releases)
