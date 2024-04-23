import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MassIssueToMfgSvc
# Description: Use this function to quickly issue all planned materials to a job,
instead of entering them individually.
Serialized parts cannot be issued using this function depending on plant serial tracking setting.
Issue transactions generated in this way reduce inventory quantities,
and post material costs to the Job.
This is a useful function if your material estimates are fairly accurate.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSetupGrp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetRows
      :param whereClauseSetupGrp: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSetupGrp=" + whereClauseSetupGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Get Available Transaction Doc Types method.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailTranDocTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildMassIssueBrowse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildMassIssueBrowse
   Description: This method is called when the user presses Issue button after entering the Job#.
This method builds and returns the Epicor.Mfg.BO.MassIssueToMfgDataSet dataset.
   OperationID: BuildMassIssueBrowse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildMassIssueBrowse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildMassIssueBrowse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMassIssueToMfg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMassIssueToMfg
   Description: Returns dataset MassIssueToMfg that contains records that can be issued/returned
   OperationID: GetMassIssueToMfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMassIssueToMfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassIssueToMfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearAll
   Description: Clear All - Clear all issued quantities
   OperationID: ClearAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClauseSetupGrp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetList
      :param whereClauseSetupGrp: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSetupGrp=" + whereClauseSetupGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetListPaging(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetListPaging
   Description: List of jobs that can be selected for Mass Issue.  This method considers server paging
   OperationID: Get_GetListPaging
      :param whereClause: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMassIssueInput(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMassIssueInput
   Description: Create a new Epicor.Mfg.BO.MassIssueInputDataSet.  Only few fields like
Company and TranDate are populated.  All other fields are dependent on
the user selecting a job#.  After the user enters a Job# call OnChangeJobNum
to populate other fields in MassIssueInputDataSet .
   OperationID: GetNewMassIssueInput
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInput_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInput_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMassIssueInputJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMassIssueInputJobNum
   Description: Create a new Epicor.Mfg.BO.MassIssueInputDataSet based on the Job# input.
   OperationID: GetNewMassIssueInputJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInputJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInputJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMassIssueInputList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMassIssueInputList
   Description: This method creates a new ttMassIssueInputList row entry.
   OperationID: GetNewMassIssueInputList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInputList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInputList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMassIssueInputMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMassIssueInputMultiple
   Description: Call this method when the user selects multiple jobs.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: GetNewMassIssueInputMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMassIssueInputMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassIssueInputMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMassIssueInputForJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMassIssueInputForJob
   Description: Call this method to return data for a specific job
   OperationID: GetMassIssueInputForJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMassIssueInputForJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassIssueInputForJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IssueAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IssueAll
   Description: Issue All - Default Issue All
   OperationID: IssueAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IssueAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IssueAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeStockCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeStockCheck
   Description: This method performs the Negative Stock check.  This procedure should be run
before calling PerformMassIssue method.
   OperationID: NegativeStockCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeStockCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeStockCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssemblySeq
   Description: To populate the MassIssueInputDataSet dataset with the fields when JobNum changes
This method populates and returns the Epicor.Mfg.BO.MassIssueInputDataSet dataset.
   OperationID: OnChangeAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBinNum
   Description: Call this method when binnum changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a new Bin number and onhandqty.
   OperationID: OnChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBinNumForSysRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBinNumForSysRow
   Description: Call this method when binNum changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a new Bin number and onhandqty.
   OperationID: OnChangeBinNumForSysRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNumForSysRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNumForSysRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method when the Job# changes in ttMassIssueInputJob.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLotNum
   Description: Call this method when Lot number changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset.
This method checks whether the user has security permissions to create lot.
   OperationID: OnChangeLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLotNumForSysRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLotNumForSysRowID
   Description: Call this method when Lot number changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset.
This method checks whether the user has security permissions to create lot.
   OperationID: OnChangeLotNumForSysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLotNumForSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNumForSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: To populate the Epicor.Mfg.BO.MassIssueToMfgDataSet dataset with the fields when PartNum changes
Call this method when PartNum changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQtyIssued(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQtyIssued
   Description: Call this method when Qty Issued changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a yes or no value for IssuedComplete.
   OperationID: OnChangeQtyIssued
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQtyIssued_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQtyIssued_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUOMCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUOMCode
   Description: Recalculates stockqty when the UOM changes.
   OperationID: OnChangeUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWareHouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWareHouse
   Description: Call this method when Ware house changes in Epicor.Mfg.BO.MassIssueToMfgDataSet dataset
It returns a new Bin number
   OperationID: OnChangeWareHouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWareHouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWareHouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnPartNumChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPartNumChanging
   Description: Call this method when the value of Part is changing for validation.
   OperationID: OnPartNumChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPartNumChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPartNumChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformMassIssue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformMassIssue
   Description: This function performs the processing required to do the Mass Issue to
manufacturing.  No transactions are committed to the database unless
this function is invoked.
Please call NegativeStockCheck method before calling PerformMassIssue.
   OperationID: PerformMassIssue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMassIssue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMassIssue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformMassIssueReturn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformMassIssueReturn
   Description: This function performs the processing required to do the Mass Issue to
Manufacturing and Mass Return from Manufacturing.  No transactions are committed to the database unless
this function is invoked.
Call NegativeStockCheck method before calling PerformMassIssueReturn.
This method returns a list that contains the keys of PartTran records created.
   OperationID: PerformMassIssueReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMassIssueReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMassIssueReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePerformMassIssueHT(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePerformMassIssueHT
   Description: Store the results of PrePerformMassIssue in hash-table htPrePerform
   OperationID: PrePerformMassIssueHT
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePerformMassIssueHT_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMassIssueHT_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePerformMassIssue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePerformMassIssue
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PrePerformMassIssue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePerformMassIssue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMassIssue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePerformMassIssueOneItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePerformMassIssueOneItem
   Description: This method will return a record in the LegalNumGenOpts datatable against the current Mtl if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PrePerformMassIssueOneItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePerformMassIssueOneItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMassIssueOneItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassIssueToMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobHeadRow] = obj["value"]
      pass

class Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.EquipSerialNum:str = obj["EquipSerialNum"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.EquipPlant:str = obj["EquipPlant"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipBrand:str = obj["EquipBrand"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipCurrentMeter:int = obj["EquipCurrentMeter"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumLocationIDNumReq:bool = obj["PartNumLocationIDNumReq"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.PlantMaintPlant:str = obj["PlantMaintPlant"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProdTeamIDDescription:str = obj["ProdTeamIDDescription"]
      self.ProdTeamIDName:str = obj["ProdTeamIDName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedCodeDescription:str = obj["SchedCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildMassIssueBrowse_input:
   """ Required : 
   ds
   ipSysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      self.ipSysRowID:str = obj["ipSysRowID"]
      """  SysRowID of the selected row.  """  
      pass

class BuildMassIssueBrowse_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearAll_input:
   """ Required : 
   pcView
   ds
   """  
   def __init__(self, obj):
      self.pcView:str = obj["pcView"]
      """  Input the filter shown in the browse.  Valid values are Open, Completed or All.  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class ClearAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.EquipSerialNum:str = obj["EquipSerialNum"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.EquipPlant:str = obj["EquipPlant"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipBrand:str = obj["EquipBrand"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipCurrentMeter:int = obj["EquipCurrentMeter"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumLocationIDNumReq:bool = obj["PartNumLocationIDNumReq"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.PlantMaintPlant:str = obj["PlantMaintPlant"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProdTeamIDDescription:str = obj["ProdTeamIDDescription"]
      self.ProdTeamIDName:str = obj["ProdTeamIDName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedCodeDescription:str = obj["SchedCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassIssueInputJobRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.IsReturn:bool = obj["IsReturn"]
      """  Indicated if it's a return from mfg  """  
      self.WarnMessage:str = obj["WarnMessage"]
      """  Warning Message if the Quantity completed on this Job was received or shipped  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassIssueInputListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.IsReturn:bool = obj["IsReturn"]
      """  Indicated if it's a return from mfg  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassIssueInputListTableset:
   def __init__(self, obj):
      self.MassIssueInputList:list[Erp_Tablesets_MassIssueInputListRow] = obj["MassIssueInputList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassIssueInputRow:
   def __init__(self, obj):
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.JobType:str = obj["JobType"]
      """  Job type  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence  """  
      self.IncludeSubassemblies:bool = obj["IncludeSubassemblies"]
      """  Include Sub assemblies  """  
      self.IncludeSubassembliesOverrun:bool = obj["IncludeSubassembliesOverrun"]
      """  Include Subassemblies' overrun quantity  """  
      self.PartNumJH:str = obj["PartNumJH"]
      """  Part Number Jobhead  """  
      self.PartDescJH:str = obj["PartDescJH"]
      """  Part Jobhead description  """  
      self.CallNum:int = obj["CallNum"]
      """  Call Number  """  
      self.CallLine:int = obj["CallLine"]
      """  Call Line  """  
      self.PartNumAsm:str = obj["PartNumAsm"]
      """  Part Number Assembly  """  
      self.PartDescAsm:str = obj["PartDescAsm"]
      """  Part Assembly description  """  
      self.Company:str = obj["Company"]
      """  Company indentifier  """  
      self.JobDescJH:str = obj["JobDescJH"]
      self.IUM:str = obj["IUM"]
      self.AssemblyQty:int = obj["AssemblyQty"]
      self.dummyKeyfield:str = obj["dummyKeyfield"]
      """  Dummy key field.  It is the primary key of the dataset  """  
      self.FSCallhdInvoiced:bool = obj["FSCallhdInvoiced"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Set to true if the user chooses Include Subassembly and the record is part of the parent assembly  """  
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.IsReturn:bool = obj["IsReturn"]
      """  Return from Mfg  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum  """  
      self.RevisionNumAsm:str = obj["RevisionNumAsm"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum  """  
      self.RevisionNumJH:str = obj["RevisionNumJH"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum  """  
      self.SysRowID:str = obj["SysRowID"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartAsmTrackInventoryByRevision:bool = obj["PartAsmTrackInventoryByRevision"]
      self.PartAsmPartDescription:str = obj["PartAsmPartDescription"]
      self.PartAsmPricePerCode:str = obj["PartAsmPricePerCode"]
      self.PartAsmTrackDimension:bool = obj["PartAsmTrackDimension"]
      self.PartAsmSellingFactor:int = obj["PartAsmSellingFactor"]
      self.PartAsmTrackLots:bool = obj["PartAsmTrackLots"]
      self.PartAsmSalesUM:str = obj["PartAsmSalesUM"]
      self.PartAsmTrackSerialNum:bool = obj["PartAsmTrackSerialNum"]
      self.PartAsmIUM:str = obj["PartAsmIUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassIssueInputTableset:
   def __init__(self, obj):
      self.MassIssueInputJob:list[Erp_Tablesets_MassIssueInputJobRow] = obj["MassIssueInputJob"]
      self.MassIssueInput:list[Erp_Tablesets_MassIssueInputRow] = obj["MassIssueInput"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassIssueJobListTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassIssueRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.Parent:int = obj["Parent"]
      """  Parent  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number  """  
      self.Description:str = obj["Description"]
      """  Part Description  """  
      self.QtyRequired:int = obj["QtyRequired"]
      """  Quantity Required  """  
      self.SaveReq:int = obj["SaveReq"]
      """  Qty Save Request  """  
      self.QtyRequiredMtl:int = obj["QtyRequiredMtl"]
      """  Original JobMtl required Qty  """  
      self.QtyIssued:int = obj["QtyIssued"]
      """  Quantity Issued  """  
      self.ProdQty:int = obj["ProdQty"]
      """  Product Quantity  """  
      self.PullQty:int = obj["PullQty"]
      """  Pull Quantity  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity Per  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  Over run quantity  """  
      self.BuildQty:int = obj["BuildQty"]
      """  Build quantity  """  
      self.RemPullQty:int = obj["RemPullQty"]
      """  Rem pull quantity  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Estimated scrap type  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated scrap  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Fixed Quantity  """  
      self.Warehouse:str = obj["Warehouse"]
      """  Ware house  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number  """  
      self.ToWarehouse:str = obj["ToWarehouse"]
      """  To Ware house  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  To Bin Number  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Issued Complete  """  
      self.CmpFlagOrig:bool = obj["CmpFlagOrig"]
      """  CmpFlagOrig  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Job complete  """  
      self.PrevIssued:int = obj["PrevIssued"]
      """  Previous issued  """  
      self.SaveIssued:int = obj["SaveIssued"]
      """  Save Issued  """  
      self.DimTrack:bool = obj["DimTrack"]
      """  Dimension tracked ?  """  
      self.LotTrack:bool = obj["LotTrack"]
      """  Track lots ?  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.UnitMeasure:str = obj["UnitMeasure"]
      """  Unit of measure  """  
      self.TranType:str = obj["TranType"]
      """  Transaction type  """  
      self.TranClass:str = obj["TranClass"]
      """  Transaction class  """  
      self.TranReference:str = obj["TranReference"]
      """  Transaction reference  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Inventory transaction  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Transaction entered by  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Cost method  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material unit cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor unit cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden unit cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontractor unit cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.IsPart:bool = obj["IsPart"]
      """  Is Part  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.PartNumJH:str = obj["PartNumJH"]
      """  Part Number Jobhead  """  
      self.PartDescJH:str = obj["PartDescJH"]
      """  Part Jobhead description  """  
      self.PartNumAsm:str = obj["PartNumAsm"]
      """  Part Number Assembly  """  
      self.PartDescAsm:str = obj["PartDescAsm"]
      """  Part Assembly description  """  
      self.PartDescMS:str = obj["PartDescMS"]
      """  Part Material sequence description  """  
      self.PartNumMS:str = obj["PartNumMS"]
      """  Part Number Material Sequence  """  
      self.JobType:str = obj["JobType"]
      """  Job type  """  
      self.CallNum:int = obj["CallNum"]
      """  Call Number  """  
      self.CallLine:int = obj["CallLine"]
      """  Call Line  """  
      self.IncludeSubassemblies:bool = obj["IncludeSubassemblies"]
      """  Include Sub assemblies  """  
      self.IncludeSubassembliesOverrun:bool = obj["IncludeSubassembliesOverrun"]
      """  Include Subassemblies' overrun quantity  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.StopAction:str = obj["StopAction"]
      self.StockQty:int = obj["StockQty"]
      self.DispStopAction:str = obj["DispStopAction"]
      """  Display value of StopAction.  """  
      self.OKToIssue:bool = obj["OKToIssue"]
      """  For UI use only.  """  
      self.JustQtyIssued:int = obj["JustQtyIssued"]
      """  For UI Use only  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      self.ThisTransaction:int = obj["ThisTransaction"]
      self.StockUOM:str = obj["StockUOM"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.PartTranPKs:str = obj["PartTranPKs"]
      self.ManualNumberSuffix:str = obj["ManualNumberSuffix"]
      """  This is the manually entered legal number suffix entered by the user.  This column only contains data when the legal number assigned to the transaction document type is a manual enter legal number.  """  
      self.RelatedOperSort:int = obj["RelatedOperSort"]
      self.AbleToIssue:bool = obj["AbleToIssue"]
      self.IsReturn:bool = obj["IsReturn"]
      """  Is Return from Mfg  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ManualPrefix:str = obj["ManualPrefix"]
      """  This is the manually entered legal number prefix. This column only contains data when the legal number assigned to the transaction document type is a manual enter legal number.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      self.ToBinNumDescription:str = obj["ToBinNumDescription"]
      self.ToWarehouseDescription:str = obj["ToWarehouseDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassIssueToMfgTableset:
   def __init__(self, obj):
      self.MassIssue:list[Erp_Tablesets_MassIssueRow] = obj["MassIssue"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_input:
   """ Required : 
   sysTranTypeID
   """  
   def __init__(self, obj):
      self.sysTranTypeID:str = obj["sysTranTypeID"]
      """  System Transaction Document Type  """  
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListPaging_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListPaging_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueJobListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClauseSetupGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSetupGrp:str = obj["whereClauseSetupGrp"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueJobListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMassIssueInputForJob_input:
   """ Required : 
   jobNum
   isReturn
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  The job number  """  
      self.isReturn:bool = obj["isReturn"]
      """  Is for return  """  
      pass

class GetMassIssueInputForJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueInputTableset] = obj["returnObj"]
      pass

class GetMassIssueToMfg_input:
   """ Required : 
   ds
   sysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID of the selected row  """  
      pass

class GetMassIssueToMfg_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewMassIssueInputJobNum_input:
   """ Required : 
   pcJobNum
   ds
   isReturn
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job number.  """  
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      self.isReturn:bool = obj["isReturn"]
      """  Is Return from Mfg  """  
      pass

class GetNewMassIssueInputJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMassIssueInputList_input:
   """ Required : 
   ds
   isReturn
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputListTableset] = obj["ds"]
      self.isReturn:bool = obj["isReturn"]
      """  Is Return from Mfg  """  
      pass

class GetNewMassIssueInputList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMassIssueInputMultiple_input:
   """ Required : 
   ds
   isReturn
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputListTableset] = obj["ds"]
      self.isReturn:bool = obj["isReturn"]
      """  Is Return from Mfg  """  
      pass

class GetNewMassIssueInputMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueInputTableset] = obj["returnObj"]
      pass

class GetNewMassIssueInput_input:
   """ Required : 
   ds
   isReturn
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      self.isReturn:bool = obj["isReturn"]
      """  Is return to mfg  """  
      pass

class GetNewMassIssueInput_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSetupGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSetupGrp:str = obj["whereClauseSetupGrp"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassIssueJobListTableset] = obj["returnObj"]
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

class IssueAll_input:
   """ Required : 
   pcView
   ds
   """  
   def __init__(self, obj):
      self.pcView:str = obj["pcView"]
      """  Input the filter shown in the browse.  Valid values are Open, Completed or All.  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class IssueAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class NegativeStockCheck_input:
   """ Required : 
   pcJobNum
   ds
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job# to which the Mass issue is to be done.  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class NegativeStockCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.pcQuestion:str = obj["parameters"]
      self.pcError:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeAssemblySeq_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      pass

class OnChangeAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBinNumForSysRow_input:
   """ Required : 
   pcWarehouse
   pcBinNum
   pcSysRowID
   ds
   """  
   def __init__(self, obj):
      self.pcWarehouse:str = obj["pcWarehouse"]
      """  Warehouse  """  
      self.pcBinNum:str = obj["pcBinNum"]
      """  New Bin number which should be checked  """  
      self.pcSysRowID:str = obj["pcSysRowID"]
      """  Current SysRowID  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeBinNumForSysRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBinNum_input:
   """ Required : 
   pcWarehouse
   pcPartNum
   pcBinNum
   ds
   """  
   def __init__(self, obj):
      self.pcWarehouse:str = obj["pcWarehouse"]
      """  Warehouse  """  
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number  """  
      self.pcBinNum:str = obj["pcBinNum"]
      """  New Bin number which should be checked  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   pcJobNum
   ds
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job Number.  """  
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueInputTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLotNumForSysRowID_input:
   """ Required : 
   plLotTrack
   pcLotNum
   plCreatePartLot
   sysRowID
   ds
   """  
   def __init__(self, obj):
      self.plLotTrack:bool = obj["plLotTrack"]
      """  Is the part lot tracked ?  """  
      self.pcLotNum:str = obj["pcLotNum"]
      """  Lot number  """  
      self.plCreatePartLot:bool = obj["plCreatePartLot"]
      """  User's answer to the question - Do you want to create a lot number  """  
      self.sysRowID:str = obj["sysRowID"]
      """  Current SysRowID  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeLotNumForSysRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLotNum_input:
   """ Required : 
   plLotTrack
   pcLotNum
   plCreatePartLot
   ds
   """  
   def __init__(self, obj):
      self.plLotTrack:bool = obj["plLotTrack"]
      """  Is the part lot tracked ?  """  
      self.pcLotNum:str = obj["pcLotNum"]
      """  Lot number  """  
      self.plCreatePartLot:bool = obj["plCreatePartLot"]
      """  User's answer to the question - Do you want to create a lot number  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   piSeqNum
   ds
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job # to which the Mass Issue is done  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  Assembly#  """  
      self.piSeqNum:int = obj["piSeqNum"]
      """  Seq Number  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQtyIssued_input:
   """ Required : 
   piAssemblySeq
   piSeqNum
   pdQtyIssued
   pdAssemblyQty
   ds
   """  
   def __init__(self, obj):
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  Assembly#  """  
      self.piSeqNum:int = obj["piSeqNum"]
      """  Seq Number  """  
      self.pdQtyIssued:int = obj["pdQtyIssued"]
      """  Proposed Quantity Issued  """  
      self.pdAssemblyQty:int = obj["pdAssemblyQty"]
      """  Current Assembly Quantity  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeQtyIssued_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.pcWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeUOMCode_input:
   """ Required : 
   pcRowIdent
   pcUOM
   pdAssemblyQty
   ds
   """  
   def __init__(self, obj):
      self.pcRowIdent:str = obj["pcRowIdent"]
      """  RowIdent of the current record  """  
      self.pcUOM:str = obj["pcUOM"]
      """  Proposed UOM  """  
      self.pdAssemblyQty:int = obj["pdAssemblyQty"]
      """  Current Assembly Quantity  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeUOMCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWareHouse_input:
   """ Required : 
   pcWarehouse
   pcPartNum
   ds
   """  
   def __init__(self, obj):
      self.pcWarehouse:str = obj["pcWarehouse"]
      """  Ware house  """  
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangeWareHouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcWarning:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   dispNumberOfPieces
   piAssemblySeq
   piSeqNum
   ds
   """  
   def __init__(self, obj):
      self.dispNumberOfPieces:int = obj["dispNumberOfPieces"]
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  Assembly#  """  
      self.piSeqNum:int = obj["piSeqNum"]
      """  Seq Number  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnPartNumChanging_input:
   """ Required : 
   pcPartNum
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  PartNum  """  
      pass

class OnPartNumChanging_output:
   def __init__(self, obj):
      pass

class PerformMassIssueReturn_input:
   """ Required : 
   pcJobNum
   pdtTranDate
   piCallNum
   plMaterialComplete
   plNegStockCheckContinue
   ds
   pcPartTranKeys
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job# to which the Mass issue is to be done.  """  
      self.pdtTranDate:str = obj["pdtTranDate"]
      """  Transaction Date  """  
      self.piCallNum:int = obj["piCallNum"]
      """  Identifies the Service Call.  """  
      self.plMaterialComplete:bool = obj["plMaterialComplete"]
      """  Material complete? - Answer to the user question - Have all materials been issued for this Service Call?  """  
      self.plNegStockCheckContinue:bool = obj["plNegStockCheckContinue"]
      """  The response to the question generated from NegativeStockCheck method.  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.pcPartTranKeys:str = obj["pcPartTranKeys"]
      """  List of keys of PartTran records created  """  
      pass

class PerformMassIssueReturn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.pcPartTranKeys:str = obj["parameters"]
      pass

      """  output parameters  """  

class PerformMassIssue_input:
   """ Required : 
   pcJobNum
   pdtTranDate
   piCallNum
   plMaterialComplete
   plNegStockCheckContinue
   ds
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job# to which the Mass issue is to be done.  """  
      self.pdtTranDate:str = obj["pdtTranDate"]
      """  Transaction Date  """  
      self.piCallNum:int = obj["piCallNum"]
      """  Identifies the Service Call.  """  
      self.plMaterialComplete:bool = obj["plMaterialComplete"]
      """  Material complete? - Answer to the user question - Have all materials been issued for this Service Call?  """  
      self.plNegStockCheckContinue:bool = obj["plNegStockCheckContinue"]
      """  The response to the question generated from NegativeStockCheck method.  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class PerformMassIssue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PrePerformMassIssueHT_input:
   """ Required : 
   ds
   htPrePerform
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.htPrePerform      #schema had no properties on an object.
      """  RequiresUserInput results HashTable  """  
      pass

class PrePerformMassIssueHT_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.htPrePerform: UNKNOW TYPE(error 2338) = obj["htPrePerform"]
      pass

      """  output parameters  """  

class PrePerformMassIssueOneItem_input:
   """ Required : 
   pdtTranDate
   ipTranDocType
   ipSysTranType
   """  
   def __init__(self, obj):
      self.pdtTranDate:str = obj["pdtTranDate"]
      """  Transaction Date  """  
      self.ipTranDocType:str = obj["ipTranDocType"]
      """  Transaction document type  """  
      self.ipSysTranType:str = obj["ipSysTranType"]
      """  System Transaction document type  """  
      pass

class PrePerformMassIssueOneItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class PrePerformMassIssue_input:
   """ Required : 
   pdtTranDate
   ipTranDocType
   ipSysTranType
   ds
   """  
   def __init__(self, obj):
      self.pdtTranDate:str = obj["pdtTranDate"]
      """  Transaction Date  """  
      self.ipTranDocType:str = obj["ipTranDocType"]
      """  Transaction document type  """  
      self.ipSysTranType:str = obj["ipSysTranType"]
      """  System Transaction document type  """  
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      pass

class PrePerformMassIssue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassIssueToMfgTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

