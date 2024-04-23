import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ProjAnalysisSvc
# Description: Project Analysis Business Object
           Temporary data tables are used to allow export/import of
           projects to/from MS Project.  Public methods are also
           available to build/delete Project Analyis data.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BuildAnalysis(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAnalysis
   Description: Call this method when the user already selected project(s) to process.
This method expects a LIST-DELIM delimited string of RowIds of all selected
Project records.
   OperationID: BuildAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAnalysis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearAnalysis(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearAnalysis
   Description: Call this method to delete or clear all ProjectAnalysis records.
This method expects that the user already confirmed that records will be deleted.
   OperationID: ClearAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAnalysis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultPctComplete(epicorHeaders = None):
   """  
   Summary: Invoke method DefaultPctComplete
   Description: Get the default Download % Complete code before passing the input parameters
for the Project Download to MS Project.  Call this method before the user
manipulate the MSP Download input parameters.  This method will return the
default value for PctComplete variable.
   OperationID: DefaultPctComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultPctComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetByProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByProjectID
   Description: This method finds the Project record by ProjectId.
   OperationID: GetByProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProjectBrw(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetProjectBrw
   Description: This method assembles the Project browse for the main data set.
   OperationID: GetProjectBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProjectBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessMSPDownload(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessMSPDownload
   Description: This method performs the actual Project Download to MS Project.  Call this
method after the user selected the Project and entered the necessary input
parameters. This method returns the data table ttMSPDownload containing all
appropriate project information. The resulting records from the ttMSPDownload
will then need to be outputted as a CSV file (comma delimited).
   OperationID: ProcessMSPDownload
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMSPDownload_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMSPDownload_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessMSPUpload(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessMSPUpload
   Description: This method performs the actual Project Upload from MS Project.  Call this
method after the user selected the Project and entered the necessary input
parameters. This method expects an input data table ttMSPUpload with data
coming from an external comma delimited file.  The ttMSPUpload table should
only contain data (i.e. if the first line of the external file is just the
field descriptions then this record should not be included in ttMSPUpload.)
   OperationID: ProcessMSPUpload
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMSPUpload_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMSPUpload_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildAnalysis_input:
   """ Required : 
   ipGuidList
   """  
   def __init__(self, obj):
      self.ipGuidList:str = obj["ipGuidList"]
      """  A RowId list of selected Project records.  """  
      pass

class BuildAnalysis_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearAnalysis_input:
   """ Required : 
   ipProjectID
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  ProjectID  """  
      pass

class ClearAnalysis_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultPctComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vPctComplete:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_MSPDownloadRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Level:int = obj["Level"]
      """  Outline Level  """  
      self.StartDate:str = obj["StartDate"]
      """  Start  """  
      self.Duration:str = obj["Duration"]
      """  Duration  """  
      self.PctComplete:int = obj["PctComplete"]
      """  % Complete  """  
      self.ResGroup:str = obj["ResGroup"]
      """  Resource Group  """  
      self.ResName:str = obj["ResName"]
      """  Resource Names  """  
      self.Predecessors:str = obj["Predecessors"]
      """  Predecessors  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MSPDownloadTableset:
   def __init__(self, obj):
      self.MSPDownload:list[Erp_Tablesets_MSPDownloadRow] = obj["MSPDownload"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MSPUploadRow:
   def __init__(self, obj):
      self.KeyID:str = obj["KeyID"]
      """  Upload ID  """  
      self.KeyName:str = obj["KeyName"]
      """  Contains the key codes for upload: TableName and Key ID  """  
      self.Outline:int = obj["Outline"]
      """  Outline Level  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date  """  
      self.FinishDate:str = obj["FinishDate"]
      """  Finish Date  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MSPUploadTableset:
   def __init__(self, obj):
      self.MSPUpload:list[Erp_Tablesets_MSPUploadRow] = obj["MSPUpload"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjAnalysisTableset:
   def __init__(self, obj):
      self.ProjectBrw:list[Erp_Tablesets_ProjectBrwRow] = obj["ProjectBrw"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjectBrwRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Description:str = obj["Description"]
      """  Full description of Project Management Code.  """  
      self.ActiveProject:bool = obj["ActiveProject"]
      """  Indicates if this Project is active.  Can be changed directly by the user during entry.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetByProjectID_input:
   """ Required : 
   ipProjectID
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The Project ID  """  
      pass

class GetByProjectID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjAnalysisTableset] = obj["returnObj"]
      pass

class GetProjectBrw_input:
   """ Required : 
   whereClauseProject
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseProject:str = obj["whereClauseProject"]
      """  Where clause to specify set of ProjectBrw records to return  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetProjectBrw_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjAnalysisTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class ProcessMSPDownload_input:
   """ Required : 
   ipProjectID
   ipPctComplete
   ipPredecessors
   ipTasks
   ipPhases
   ipJobs
   ipJobAsm
   ipJobOper
   ipDuration
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The project ID of the selected Project.  """  
      self.ipPctComplete:str = obj["ipPctComplete"]
      """  The Download Percent Complete code.  """  
      self.ipPredecessors:bool = obj["ipPredecessors"]
      """  Include Predecessors in the download.  """  
      self.ipTasks:bool = obj["ipTasks"]
      """  Include Tasks in the download.  """  
      self.ipPhases:bool = obj["ipPhases"]
      """  Include Phases in the download.  """  
      self.ipJobs:bool = obj["ipJobs"]
      """  Include Jobs in the download.  """  
      self.ipJobAsm:bool = obj["ipJobAsm"]
      """  Include Job Assemblies in the download.  """  
      self.ipJobOper:bool = obj["ipJobOper"]
      """  Include Job Operations in the download.  """  
      self.ipDuration:str = obj["ipDuration"]
      """  The operation duration unit (Days or Hours).  """  
      pass

class ProcessMSPDownload_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MSPDownloadTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessMSPUpload_input:
   """ Required : 
   ipProjectID
   ipPhases
   ipTasks
   ipProjJobs
   ipPhaseTasks
   ipPhaseJobs
   ipPhaseStart
   ipPhaseEnd
   ipTaskStart
   ipTaskEnd
   ipJobStart
   ipJobEnd
   ds
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The project ID of the selected Project.  """  
      self.ipPhases:bool = obj["ipPhases"]
      """  Indicates if Phases should be created.  """  
      self.ipTasks:bool = obj["ipTasks"]
      """  Indicates if Tasks should be created.  """  
      self.ipProjJobs:bool = obj["ipProjJobs"]
      """  Indicates if Project and Job links should be updated.  """  
      self.ipPhaseTasks:bool = obj["ipPhaseTasks"]
      """  Indicates if Phase and Task links should be updated.  """  
      self.ipPhaseJobs:bool = obj["ipPhaseJobs"]
      """  Indicates if Phase and Job links should be updated.  """  
      self.ipPhaseStart:bool = obj["ipPhaseStart"]
      """  Indicates if Phase Start Date should be updated.  """  
      self.ipPhaseEnd:bool = obj["ipPhaseEnd"]
      """  Indicates if Phase End Date should be updated.  """  
      self.ipTaskStart:bool = obj["ipTaskStart"]
      """  Indicates if Task Start Date should be updated.  """  
      self.ipTaskEnd:bool = obj["ipTaskEnd"]
      """  Indicates if Task End Date should be updated.  """  
      self.ipJobStart:bool = obj["ipJobStart"]
      """  Indicates if Job Start Date should be updated.  """  
      self.ipJobEnd:bool = obj["ipJobEnd"]
      """  Indicates if Job End Date should be updated.  """  
      self.ds:list[Erp_Tablesets_MSPUploadTableset] = obj["ds"]
      pass

class ProcessMSPUpload_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MSPUploadTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

