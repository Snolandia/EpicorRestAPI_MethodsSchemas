import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OrderAllocSvc
# Description: Order Allocation data set
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderAllocListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AllocateByLotBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AllocateByLotBin
   Description: Allocate sales demand records by choosing specific Lots and/or Bins
   OperationID: AllocateByLotBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AllocateByLotBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllocateByLotBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AllocateBySerialNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AllocateBySerialNum
   Description: Allocate demand by choosing specific Serial Numbers
   OperationID: AllocateBySerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AllocateBySerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllocateBySerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoAllocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoAllocation
   Description: Auto allocate demand
   OperationID: AutoAllocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoAllocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoAllocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoPick(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoPick
   Description: Auto Pick demand
   OperationID: AutoPick
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoPick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoPick_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoReserve(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoReserve
   Description: Auto reserve demand
   OperationID: AutoReserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoAllocateListOfJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoAllocateListOfJobs
   Description: Allocate a list of job materials
   OperationID: AutoAllocateListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoAllocateListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoAllocateListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoReserveListOfJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoReserveListOfJobs
   Description: Reserve a list of job materials
   OperationID: AutoReserveListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserveListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserveListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoReserveJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoReserveJob
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">Job Number</param><param name="ipAssemblySeq">AssemblySeq - can be zero</param><param name="ipCutoffDate">Cutoff Date - can be blank</param><returns>The AutoReserveJob data set</returns>
   OperationID: AutoReserveJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserveJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserveJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoUnreserveJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoUnreserveJob
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">Job Number</param><param name="ipAssemblySeq">AssemblySeq - can be zero</param><param name="ipCutoffDate">Cutoff Date - can be blank</param>
   OperationID: AutoUnreserveJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoUnreserveJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoUnreserveJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Rebuild the AllocSupply list when the part number changes.  Prior to calling this
procedure, the RowMod field in all OrderAllocSupply records must be set to "U":U
because these records need to be cleared from the table before rebuilding the list.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStageBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStageBin
   Description: Validate the StageBin field
   OperationID: ChangeStageBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStageBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStageBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStagingWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStagingWarehouse
   Description: Default the staging bin based on the staging warehouse code passed in.
   OperationID: ChangeStagingWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStagingWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStagingWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDates
   Description: Check Dates, return any warnings
   OperationID: CheckDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateWave(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateWave
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipWaveDesc">Wave Description</param><param name="ipDemandType">Demand Type - valid values are Order/Job/Transfer</param><param name="opWaveNum">New Wave Number</param>
   OperationID: CreateWave
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateWave_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateWave_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCalcPref(epicorHeaders = None):
   """  
   Summary: Invoke method GetCalcPref
   Description: Purpose:
Parameters:  none
Notes:
<param name="opCalcFulfillOnSearch">Should calculations be executed after search? Yes/No</param>
   OperationID: GetCalcPref
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCalcPref_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFWBFulfillFromDemandWhseOnly(epicorHeaders = None):
   """  
   Summary: Invoke method GetFWBFulfillFromDemandWhseOnly
   Description: Purpose:
Parameters:  none
Notes:
<param name="opFWBFulfillFromDemandWhseOnly">FWB Fulfill From Demand Warehouse Only? Yes/No</param>
   OperationID: GetFWBFulfillFromDemandWhseOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFWBFulfillFromDemandWhseOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFWBLimitedRefresh(epicorHeaders = None):
   """  
   Summary: Invoke method GetFWBLimitedRefresh
   Description: Purpose:
Parameters:  none
Notes:
<param name="opFWBLimitedRefresh">FWB Limited refresh? Yes/No</param>
   OperationID: GetFWBLimitedRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFWBLimitedRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, NO_COMPANY, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Gets List of order records that can be selected for Order Allocation.
   OperationID: Get_GetList
      :param whereClause: Desc: where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param NO_COMPANY: Desc: NO_COMPANY   Required: True   Allow empty value : True
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "NO_COMPANY=" + NO_COMPANY

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListAdvanced(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListAdvanced
   Description: Gets List of order records that can be selected for fulfillment.
   OperationID: GetListAdvanced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAdvanced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAdvanced_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_callGetListBasicSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method callGetListBasicSearch
   Description: pre call to build params from "Basic" search screen
   OperationID: callGetListBasicSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListBasicSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListBasicSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListBasicSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListBasicSearch
   Description: Called from "Basic" search screen
   OperationID: GetListBasicSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBasicSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBasicSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the OrderAlloc records which will be a subset
of the PartDtl records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFWB(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFWB
   Description: Gets List of order records that can be selected for Order Allocation.
            
GetListFWB is used by programs that want to filter GetList results using the Ready to Fulfill flag (example: Fulfillment Workbench)
GetList is available for programs that do not want to consider the Ready to Fulfill flag (example: PartTracker)
   OperationID: GetListFWB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFWB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFWB_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListAndOrderAllocationGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListAndOrderAllocationGetRows
   Description: Executes GetList using a whereClause passed by the caller
and uses that ds to call OrderAllocationGetRows, which refreshes rows data only for the selected list rows.
            
For BO calls such as the REST equivalent of the PartTracker retrieval of Allocation data
   OperationID: GetListAndOrderAllocationGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAndOrderAllocationGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAndOrderAllocationGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_callGetListOfJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method callGetListOfJobs
   Description: pre call to build List params from GetListOfJobs search.
   OperationID: callGetListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfJobs
   Description: Gets List of Job records that can be selected for fulfillment.
   OperationID: GetListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_callGetListOfOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method callGetListOfOrders
   Description: pre call to build params from "GetListOfOrders" search
   OperationID: callGetListOfOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListOfOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListOfOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfOrders
   Description: Gets List of order records that can be selected for Order Allocation.
   OperationID: GetListOfOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_callGetListOfTransferOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method callGetListOfTransferOrders
   Description: pre call to build List params from GetListOfTransferOrders search.
   OperationID: callGetListOfTransferOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListOfTransferOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListOfTransferOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfTransferOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfTransferOrders
   Description: Gets List of Transfer Order records that can be selected for fulfillment.
   OperationID: GetListOfTransferOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfTransferOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfTransferOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLotBinOnHand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLotBinOnHand
   Description: Select OrderAlloc rows based on criteria.
   OperationID: GetLotBinOnHand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotBinOnHand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotBinOnHand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLotBinOnHandByWhseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLotBinOnHandByWhseCode
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetLotBinOnHandByWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotBinOnHandByWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotBinOnHandByWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLotBinOnHandByWhseCodeZoneBinType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLotBinOnHandByWhseCodeZoneBinType
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetLotBinOnHandByWhseCodeZoneBinType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotBinOnHandByWhseCodeZoneBinType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotBinOnHandByWhseCodeZoneBinType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderAllocFields(epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderAllocFields
   Description: Returns a DataSet containing a list of the OrderAlloc fields for use in the Selection Filter in Fulfillment Workbench
   OperationID: GetOrderAllocFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderAllocFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the OrderAlloc records which will be a subset
of the PartDtl records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNumOnHand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNumOnHand
   Description: Select OrderAlloc rows based on criteria.
   OperationID: GetSerialNumOnHand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumOnHand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumOnHand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNumOnHandByWhseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNumOnHandByWhseCode
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetSerialNumOnHandByWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumOnHandByWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumOnHandByWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNumOnHandByWhseCodeZoneBinType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNumOnHandByWhseCodeZoneBinType
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetSerialNumOnHandByWhseCodeZoneBinType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumOnHandByWhseCodeZoneBinType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumOnHandByWhseCodeZoneBinType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSubmitOptionsList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSubmitOptionsList
   Description: Returns a delimited list of the pick options in code`Description format.  Each
code-Description entry is separated with character ~.
   OperationID: GetSubmitOptionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubmitOptionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetWarehouseInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWarehouseInfo
   Description: This method returns the input warehouse and bin for a given job material record.
   OperationID: GetWarehouseInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarehouseInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouseInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWhseTeamUserList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWhseTeamUserList
   Description: Returns the list of all employees from Database Table WhseGroupEmp
   OperationID: GetWhseTeamUserList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhseTeamUserList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhseTeamUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_JobMtlUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method JobMtlUpdate
   Description: Update the JobMtl database table with changes saved to the OrderAlloc datatable.
   OperationID: JobMtlUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/JobMtlUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/JobMtlUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassAssign(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassAssign
   Description: Mass assign data in various columns as defined by user
   OperationID: MassAssign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAssign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAssign_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MtlQueueUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MtlQueueUpdate
   Description: Material Queue Update
   OperationID: MtlQueueUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MtlQueueUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MtlQueueUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWaveNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWaveNum
   Description: OnChangeWaveNum
   OperationID: OnChangeWaveNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWaveNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWaveNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OneDemandType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OneDemandType
   Description: Only one Demand Type can be selected
   OperationID: OneDemandType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OneDemandType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OneDemandType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OrderAllocationGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OrderAllocationGetRows
   Description: Returns the full dataset.
   OperationID: OrderAllocationGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OrderAllocationGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OrderAllocationGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OrderAllocSupplyUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OrderAllocSupplyUpdate
   Description: Update the PartAlloc database table with changes saved to the OrderAllocSupply datatable.
   OperationID: OrderAllocSupplyUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OrderAllocSupplyUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OrderAllocSupplyUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OrderRelUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OrderRelUpdate
   Description: Update the OrderRel database table with changes saved to the OrderAlloc datatable.
   OperationID: OrderRelUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OrderRelUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OrderRelUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Recalculate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Recalculate
   Description: Recalculate public method - called from Refresh Fulfillment button in Fulfillment Workbench
   OperationID: Recalculate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Recalculate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Recalculate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalculateWithSorting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalculateWithSorting
   Description: RecalculateWithSorting public method - called from Refresh Fulfillment button in Fulfillment Workbench and sorts records based on sort parameters
   OperationID: RecalculateWithSorting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalculateWithSorting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalculateWithSorting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshSelectedRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshSelectedRows
   Description: Inputs a full dataset that has been filtered by the UI to only contain the
selected rows.  It uses the full dataset to build a list dataset to be used
to call OrderAllocationGetRows which returns those rows to be returned to the
UI to refresh only the selected rows.
   OperationID: RefreshSelectedRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshSelectedRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshSelectedRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectForProcessing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectForProcessing
   Description: Select OrderAlloc rows based on criteria.
   OperationID: SelectForProcessing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectForProcessing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectForProcessing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetCalcPref(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCalcPref
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCalcFulfillOnSearch">Value to set UserComp.CalcFulfillOnSearch Yes/No</param>
   OperationID: SetCalcPref
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCalcPref_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCalcPref_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetFWBFulfillFromDemandWhseOnly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetFWBFulfillFromDemandWhseOnly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipFWBFulfillFromDemandWhseOnly">Value to set UserComp.FWBFulfillFromDemandWhseOnly Yes/No</param>
   OperationID: SetFWBFulfillFromDemandWhseOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFWBFulfillFromDemandWhseOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFWBFulfillFromDemandWhseOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetFWBLimitedRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetFWBLimitedRefresh
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipFWBLimitedRefresh">Value to set UserComp.FWBLimitedRefresh Yes/No</param>
   OperationID: SetFWBLimitedRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFWBLimitedRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFWBLimitedRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubmitForPicking(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitForPicking
   Description: Submit order releases for picking
   OperationID: SubmitForPicking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitForPicking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForPicking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TFOrdDtlUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TFOrdDtlUpdate
   Description: Update the TFOrdDtl database table with changes saved to the OrderAlloc datatable.
   OperationID: TFOrdDtlUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TFOrdDtlUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFOrdDtlUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnallocateAndReserve(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnallocateAndReserve
   Description: Unallocate and Unreserve demand records
   OperationID: UnallocateAndReserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnallocateAndReserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnallocateAndReserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnallocateAndUnreserve(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnallocateAndUnreserve
   Description: Unallocate and Unreserve sales demand records
   OperationID: UnallocateAndUnreserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnallocateAndUnreserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnallocateAndUnreserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Unreserve(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Unreserve
   Description: Unreserve demand
   OperationID: Unreserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unreserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unreserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSearchSortDefault(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSearchSortDefault
   Description: This methods will return all the Search Sort Defaults defined in the Plant Configuration
   OperationID: GetSearchSortDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSearchSortDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchSortDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderAllocListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderAllocListRow] = obj["value"]
      pass

class Erp_Tablesets_OrderAllocListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.OrderNumLineRel:str = obj["OrderNumLineRel"]
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.JobAssemblyMtl:str = obj["JobAssemblyMtl"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNumTFOrdLine:str = obj["TFOrdNumTFOrdLine"]
      self.DemandType:str = obj["DemandType"]
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      self.FromPlant:str = obj["FromPlant"]
      self.JobType:str = obj["JobType"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.Plant:str = obj["Plant"]
      self.PriorityCode:str = obj["PriorityCode"]
      self.RequestDate:str = obj["RequestDate"]
      self.RequiredDate:str = obj["RequiredDate"]
      self.ToPlant:str = obj["ToPlant"]
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the sales order release is ready to be fulfilled.  """  
      self.PartDescription:str = obj["PartDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AllocateByLotBin_input:
   """ Required : 
   ds
   cIPWhseList
   cWhseType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cIPWhseList:str = obj["cIPWhseList"]
      """  The list of warehouses  """  
      self.cWhseType:str = obj["cWhseType"]
      """  All or primary warehouse only  """  
      pass

class AllocateByLotBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      self.lReleased:bool = obj["lReleased"]
      pass

      """  output parameters  """  

class AllocateBySerialNum_input:
   """ Required : 
   ds
   cIPWhseList
   cWhseType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cIPWhseList:str = obj["cIPWhseList"]
      """  The list of warehouses  """  
      self.cWhseType:str = obj["cWhseType"]
      """  All or primary warehouse only  """  
      pass

class AllocateBySerialNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      self.lReleased:bool = obj["lReleased"]
      pass

      """  output parameters  """  

class AutoAllocateListOfJobs_input:
   """ Required : 
   orderAllocListTS
   allocTemplateID
   """  
   def __init__(self, obj):
      self.orderAllocListTS:list[Erp_Tablesets_OrderAllocListTableset] = obj["orderAllocListTS"]
      self.allocTemplateID:str = obj["allocTemplateID"]
      """  Allocation Template ID to use when allocating  """  
      pass

class AutoAllocateListOfJobs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class AutoAllocation_input:
   """ Required : 
   ds
   cIPWhseList
   cWhseType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cIPWhseList:str = obj["cIPWhseList"]
      """  The list of warehouses  """  
      self.cWhseType:str = obj["cWhseType"]
      """  All or primary warehouse only  """  
      pass

class AutoAllocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      self.lReleased:bool = obj["lReleased"]
      pass

      """  output parameters  """  

class AutoPick_input:
   """ Required : 
   ds
   cIPWhseList
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cIPWhseList:str = obj["cIPWhseList"]
      """  The list of warehouses  """  
      pass

class AutoPick_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.o_Success:bool = obj["o_Success"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class AutoReserveJob_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipCutoffDate
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      self.ipCutoffDate:str = obj["ipCutoffDate"]
      pass

class AutoReserveJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AutoReserveJobTableset] = obj["returnObj"]
      pass

class AutoReserveListOfJobs_input:
   """ Required : 
   orderAllocListTS
   """  
   def __init__(self, obj):
      self.orderAllocListTS:list[Erp_Tablesets_OrderAllocListTableset] = obj["orderAllocListTS"]
      pass

class AutoReserveListOfJobs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class AutoReserve_input:
   """ Required : 
   ds
   cIPWhseList
   cWhseType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SlimOrderAllocTableset] = obj["ds"]
      self.cIPWhseList:str = obj["cIPWhseList"]
      """  The list of warehouses  """  
      self.cWhseType:str = obj["cWhseType"]
      """  All or primary warehouse only  """  
      pass

class AutoReserve_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SlimOrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class AutoUnreserveJob_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipCutoffDate
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      self.ipCutoffDate:str = obj["ipCutoffDate"]
      pass

class AutoUnreserveJob_output:
   def __init__(self, obj):
      pass

class ChangePartNum_input:
   """ Required : 
   ds
   cPartNum
   iOrderNum
   iOrderLine
   iOrderRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cPartNum:str = obj["cPartNum"]
      """  The part number  """  
      self.iOrderNum:int = obj["iOrderNum"]
      """  The order number  """  
      self.iOrderLine:int = obj["iOrderLine"]
      """  The order line  """  
      self.iOrderRelNum:int = obj["iOrderRelNum"]
      """  The order release number  """  
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeStageBin_input:
   """ Required : 
   ds
   proposedStageBin
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.proposedStageBin:str = obj["proposedStageBin"]
      """  The proposed bin  """  
      pass

class ChangeStageBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeStagingWarehouse_input:
   """ Required : 
   ds
   cProposedStageWhseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cProposedStageWhseCode:str = obj["cProposedStageWhseCode"]
      """  The proposed warehouse code  """  
      pass

class ChangeStagingWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDates_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SlimOrderAllocTableset] = obj["ds"]
      pass

class CheckDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SlimOrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateWave_input:
   """ Required : 
   ipWaveDesc
   ipDemandType
   """  
   def __init__(self, obj):
      self.ipWaveDesc:str = obj["ipWaveDesc"]
      self.ipDemandType:str = obj["ipDemandType"]
      pass

class CreateWave_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWaveNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_AutoReserveJobRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.IUM:str = obj["IUM"]
      self.ReservedQty:int = obj["ReservedQty"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      self.PickingQty:int = obj["PickingQty"]
      self.PickedQty:int = obj["PickedQty"]
      self.FulfilledQty:int = obj["FulfilledQty"]
      self.RemainingToReserve:int = obj["RemainingToReserve"]
      self.PartWhseOnHandQty:int = obj["PartWhseOnHandQty"]
      self.UnreservedInventory:int = obj["UnreservedInventory"]
      self.PartNum:str = obj["PartNum"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  AttrClassID  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  AttributeSetID  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute S  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AutoReserveJobTableset:
   def __init__(self, obj):
      self.AutoReserveJob:list[Erp_Tablesets_AutoReserveJobRow] = obj["AutoReserveJob"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OrderAllocListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.OrderNumLineRel:str = obj["OrderNumLineRel"]
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.JobAssemblyMtl:str = obj["JobAssemblyMtl"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNumTFOrdLine:str = obj["TFOrdNumTFOrdLine"]
      self.DemandType:str = obj["DemandType"]
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      self.FromPlant:str = obj["FromPlant"]
      self.JobType:str = obj["JobType"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.Plant:str = obj["Plant"]
      self.PriorityCode:str = obj["PriorityCode"]
      self.RequestDate:str = obj["RequestDate"]
      self.RequiredDate:str = obj["RequiredDate"]
      self.ToPlant:str = obj["ToPlant"]
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the sales order release is ready to be fulfilled.  """  
      self.PartDescription:str = obj["PartDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderAllocListTableset:
   def __init__(self, obj):
      self.OrderAllocList:list[Erp_Tablesets_OrderAllocListRow] = obj["OrderAllocList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OrderAllocRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  """  
      self.Make:bool = obj["Make"]
      """   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  """  
      self.OurJobQty:int = obj["OurJobQty"]
      """  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  """  
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      """  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This field identifies Buy To Order releases.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  """  
      self.IUM:str = obj["IUM"]
      """   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  """  
      self.SalesUM:str = obj["SalesUM"]
      """   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DispOrderShippedQty:int = obj["DispOrderShippedQty"]
      self.DispOrderRemainingQty:int = obj["DispOrderRemainingQty"]
      self.DispOurStockShippedQty:int = obj["DispOurStockShippedQty"]
      self.DispOurJobShippedQty:int = obj["DispOurJobShippedQty"]
      self.DispOrderReserved:int = obj["DispOrderReserved"]
      self.DispOrderMfgReserved:int = obj["DispOrderMfgReserved"]
      self.DispOrderStockReserved:int = obj["DispOrderStockReserved"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZip:str = obj["ShipToZip"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.StagingWhseDescription:str = obj["StagingWhseDescription"]
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      self.StageWhseCode:str = obj["StageWhseCode"]
      self.StageBin:str = obj["StageBin"]
      self.EnableSelectForPicking:bool = obj["EnableSelectForPicking"]
      self.OrderNumLineRel:str = obj["OrderNumLineRel"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      self.SupplyPartNum:str = obj["SupplyPartNum"]
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      self.CustGroupCode:str = obj["CustGroupCode"]
      self.KitParentPartNum:str = obj["KitParentPartNum"]
      self.KitParentLine:int = obj["KitParentLine"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.ReservedQty:int = obj["ReservedQty"]
      self.PickingQty:int = obj["PickingQty"]
      self.PickedQty:int = obj["PickedQty"]
      self.RemainingToReserve:int = obj["RemainingToReserve"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.UnreservedInventory:int = obj["UnreservedInventory"]
      self.AvailablePercent:int = obj["AvailablePercent"]
      self.OrderRelShippedTotal:int = obj["OrderRelShippedTotal"]
      self.OrderedLessShipped:int = obj["OrderedLessShipped"]
      self.PartWhseOnHandQty:int = obj["PartWhseOnHandQty"]
      self.KitFulfillmentValuePct:int = obj["KitFulfillmentValuePct"]
      self.KitFulfilledValuePct:int = obj["KitFulfilledValuePct"]
      self.PotentialReserveQty:int = obj["PotentialReserveQty"]
      self.FulfilledQtyPct:int = obj["FulfilledQtyPct"]
      self.FulfillmentQtyPct:int = obj["FulfillmentQtyPct"]
      self.PartVolume:int = obj["PartVolume"]
      self.PartWeight:int = obj["PartWeight"]
      self.KitFlag:str = obj["KitFlag"]
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      self.NeedsUpdate:bool = obj["NeedsUpdate"]
      self.KitShipComplete:bool = obj["KitShipComplete"]
      self.KitQtyPer:int = obj["KitQtyPer"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      self.ReservedQtyPct:int = obj["ReservedQtyPct"]
      self.AllocatedQtyPct:int = obj["AllocatedQtyPct"]
      self.FulfilledQty:int = obj["FulfilledQty"]
      self.WaveNum:int = obj["WaveNum"]
      self.WaveDestBinNum:str = obj["WaveDestBinNum"]
      self.WavePickTicketPrinted:bool = obj["WavePickTicketPrinted"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackMultipleUOM:bool = obj["PartTrackMultipleUOM"]
      self.BTCustNum:int = obj["BTCustNum"]
      self.BTCustID:str = obj["BTCustID"]
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      self.CreditHold:bool = obj["CreditHold"]
      self.BTCustName:str = obj["BTCustName"]
      self.AllocatedUM:str = obj["AllocatedUM"]
      self.ReservedUM:str = obj["ReservedUM"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNumTFOrdLine:str = obj["TFOrdNumTFOrdLine"]
      self.DemandType:str = obj["DemandType"]
      """  valid values: Order, Job or Transfer  """  
      self.DemandKey1:str = obj["DemandKey1"]
      """  OrderRel.OrderNum, JobMtl.JobNum or TFOrdHed.TFOrdNum  """  
      self.DemandKey2:str = obj["DemandKey2"]
      """  OrderRel.OrderLine, JobMtl.AssemblySeq or TFOrdDtl.TFOrdLine  """  
      self.DemandKey3:str = obj["DemandKey3"]
      """  OrderRel.OrderRelNum, JobMtl.MtlSeq  """  
      self.JobAssemblyMtl:str = obj["JobAssemblyMtl"]
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      self.FulfillmentSeq:int = obj["FulfillmentSeq"]
      """  The order in which the demand records should be Fulfilled.  """  
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      self.OrderFulfillmentPct:int = obj["OrderFulfillmentPct"]
      self.ReservePriorityOverride:int = obj["ReservePriorityOverride"]
      self.CustCategory:str = obj["CustCategory"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.PartWeightUOM:str = obj["PartWeightUOM"]
      self.NormalizedPartWeight:int = obj["NormalizedPartWeight"]
      self.NormalizedPartWeightUOM:str = obj["NormalizedPartWeightUOM"]
      self.NormalizedPartVolume:int = obj["NormalizedPartVolume"]
      self.NormalizedPartVolumeUOM:str = obj["NormalizedPartVolumeUOM"]
      self.PartVolumeUOM:str = obj["PartVolumeUOM"]
      self.UnitPriceCurrencyCode:str = obj["UnitPriceCurrencyCode"]
      self.TotalValue:int = obj["TotalValue"]
      self.TotalVolume:int = obj["TotalVolume"]
      self.TotalWeight:int = obj["TotalWeight"]
      self.FulfillmentValue:int = obj["FulfillmentValue"]
      self.FulfillmentValuePct:int = obj["FulfillmentValuePct"]
      self.FulfilledValue:int = obj["FulfilledValue"]
      self.FulfilledValuePct:int = obj["FulfilledValuePct"]
      self.OrderProjectID:str = obj["OrderProjectID"]
      self.UDShortChar01:str = obj["UDShortChar01"]
      self.UDShortChar02:str = obj["UDShortChar02"]
      self.UDNumber01:int = obj["UDNumber01"]
      self.UDNumber02:int = obj["UDNumber02"]
      self.UDCheckbox01:bool = obj["UDCheckbox01"]
      self.UDCheckbox02:bool = obj["UDCheckbox02"]
      self.UDDate01:str = obj["UDDate01"]
      self.UDDate02:str = obj["UDDate02"]
      self.OrderCounterSale:bool = obj["OrderCounterSale"]
      self.DistributionType:str = obj["DistributionType"]
      self.WaveDesc:str = obj["WaveDesc"]
      self.TFOrdToPlant:str = obj["TFOrdToPlant"]
      self.TFOrdToPlantName:str = obj["TFOrdToPlantName"]
      self.TFOrdToPlantCity:str = obj["TFOrdToPlantCity"]
      self.TFOrdToPlantState:str = obj["TFOrdToPlantState"]
      self.TFOrdToPlantZip:str = obj["TFOrdToPlantZip"]
      self.TFOrdToPlantCountry:str = obj["TFOrdToPlantCountry"]
      self.TFOrdFromPlant:str = obj["TFOrdFromPlant"]
      self.TFOrdFromWarehouseCode:str = obj["TFOrdFromWarehouseCode"]
      self.PartProdCode:str = obj["PartProdCode"]
      self.LineCount:int = obj["LineCount"]
      self.OrderStatus:str = obj["OrderStatus"]
      self.JobStatus:str = obj["JobStatus"]
      self.TFOrdStatus:str = obj["TFOrdStatus"]
      self.CustRegionCode:str = obj["CustRegionCode"]
      self.JobStartDate:str = obj["JobStartDate"]
      self.JobSchedCode:str = obj["JobSchedCode"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.ReleaseCount:int = obj["ReleaseCount"]
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      self.OrderHeld:bool = obj["OrderHeld"]
      self.BackFlush:bool = obj["BackFlush"]
      """  Used to indicate if the Job Material is backflush.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      self.OrderPONum:str = obj["OrderPONum"]
      self.OrderAllocSupplyCounter:int = obj["OrderAllocSupplyCounter"]
      self.KitOurReqQty:int = obj["KitOurReqQty"]
      self.KitUnitPrice:int = obj["KitUnitPrice"]
      self.KitExtPrice:int = obj["KitExtPrice"]
      self.KitPricing:str = obj["KitPricing"]
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.FilterAttributeSetID:int = obj["FilterAttributeSetID"]
      """  The attribute set ID specified here is used to filter the part bin locations displayed when allocating by lot/bin.  """  
      self.FilterAttributeSetShortDescription:str = obj["FilterAttributeSetShortDescription"]
      """  The short description of the filter attribute set.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.MtoAvailQty:int = obj["MtoAvailQty"]
      """  The quantity of a make direct sales order release that can be released for picking from manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderAllocSupplyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.JobNum:str = obj["JobNum"]
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.AllocatedQuantity:int = obj["AllocatedQuantity"]
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.ReservedQuantity:int = obj["ReservedQuantity"]
      self.SupplySource:str = obj["SupplySource"]
      self.OrderNumLineRel:str = obj["OrderNumLineRel"]
      self.WIPQuantity:int = obj["WIPQuantity"]
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      self.DemandType:str = obj["DemandType"]
      self.DemandKey1:str = obj["DemandKey1"]
      self.DemandKey2:str = obj["DemandKey2"]
      self.DemandKey3:str = obj["DemandKey3"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.UOM:str = obj["UOM"]
      self.PickingQuantity:int = obj["PickingQuantity"]
      self.PickedQuantity:int = obj["PickedQuantity"]
      self.UnreservedQuantity:int = obj["UnreservedQuantity"]
      self.FulfilledQuantity:int = obj["FulfilledQuantity"]
      self.JobAssemblyMtl:str = obj["JobAssemblyMtl"]
      self.TFOrdNumTFOrdLine:str = obj["TFOrdNumTFOrdLine"]
      self.DisplaySeq:int = obj["DisplaySeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderAllocTableset:
   def __init__(self, obj):
      self.OrderAlloc:list[Erp_Tablesets_OrderAllocRow] = obj["OrderAlloc"]
      self.OrderAllocSupply:list[Erp_Tablesets_OrderAllocSupplyRow] = obj["OrderAllocSupply"]
      self.PartAlloc:list[Erp_Tablesets_PartAllocRow] = obj["PartAlloc"]
      self.PartAllocLot:list[Erp_Tablesets_PartAllocLotRow] = obj["PartAllocLot"]
      self.PartAllocSerial:list[Erp_Tablesets_PartAllocSerialRow] = obj["PartAllocSerial"]
      self.PartAllocTran:list[Erp_Tablesets_PartAllocTranRow] = obj["PartAllocTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAllocLotRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the allocation is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity allocated is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is allocated.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is allocated.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is allocated.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is allocated.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is allocated.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is allocated.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is allocated.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is allocated.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.DimCode:str = obj["DimCode"]
      """  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  """  
      self.Allocate:bool = obj["Allocate"]
      self.Unallocate:bool = obj["Unallocate"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.NewAllocatedQty:int = obj["NewAllocatedQty"]
      self.Batch:str = obj["Batch"]
      self.MfgBatch:str = obj["MfgBatch"]
      self.MfgLot:str = obj["MfgLot"]
      self.HeatNum:str = obj["HeatNum"]
      self.FirmWare:str = obj["FirmWare"]
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      self.MfgDt:str = obj["MfgDt"]
      self.CureDt:str = obj["CureDt"]
      self.ExpirationDate:str = obj["ExpirationDate"]
      self.PCID:str = obj["PCID"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      """  Attribute Class ID for the part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the allocation is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity allocated is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is allocated.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is allocated.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is allocated.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is allocated.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is allocated.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is allocated.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is allocated.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is allocated.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.DimCode:str = obj["DimCode"]
      """  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """   Quantity that is "Reserved" for the demand (sales order/job requirement).   Reservations for Orders are made via the Order Allocations program.
(Also see PartWhse.SalesReservedQty, JobHead.ReservedQty)  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  """  
      self.PickingQty:int = obj["PickingQty"]
      """   Quantity that is in the picking process for a sales order.  Orders are selected for picking in the Order Allocations program.
Picking is another category of Hard Allocations which are excluded from available quantiity calculations"
(Also see PartWhse.SalesPickingQty)  """  
      self.PickedQty:int = obj["PickedQty"]
      """   Quantity that has been picked a sales order.  Orders are picked when the material mover enters the  move transaction or if the staging whse/bin area is the same as the source whse/bin
Picked is another category of Hard Allocations which are excluded from available quantiity calculations"

(Also see PartWhse.SalesPickingQty)  """  
      self.DemandType:str = obj["DemandType"]
      """  Valid values: Order, Job or Transfer.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation Date  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.WaveNum:int = obj["WaveNum"]
      """  Wave Number.  """  
      self.WaveDestBinNum:str = obj["WaveDestBinNum"]
      """  The user defined bin number within the warehouse to which the inventory in this Wave Allocation should be moved via a Bin-To-Bin move.  """  
      self.WavePickTicketPrinted:bool = obj["WavePickTicketPrinted"]
      """  When PartAlloc.WaveNum <> 0, a Wave Pick Ticket must be printed to move the inventory from the current bin to the destination bin.  This flag indicates if the Wave Pick Ticket has been printed.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SearchSort:str = obj["SearchSort"]
      """  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type.  Valid values:  Standard, Managed or Both.  """  
      self.BinNumFirstOption:str = obj["BinNumFirstOption"]
      """  The first option for the bin from which to select inventory within the warehouse.  """  
      self.WhseDestWarehouseCode:str = obj["WhseDestWarehouseCode"]
      """  Warehouse Destination for the allocated qty.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.CrossDocking:bool = obj["CrossDocking"]
      """  True if Cross-Docking is enabled.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.MultiplePartsPerBin:bool = obj["MultiplePartsPerBin"]
      """  True if Multiple Parts Per Bin is allowed.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.BinNumProductionIn:str = obj["BinNumProductionIn"]
      """  The user defined Production In bin number within the warehouse.  """  
      self.ForwardStageGroup:str = obj["ForwardStageGroup"]
      """  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  """  
      self.HardAllocation:bool = obj["HardAllocation"]
      """  Hard Allocation  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema Name of the related row.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table Name of the related row.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID of the related row.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.DemandKey1:str = obj["DemandKey1"]
      self.DemandKey2:str = obj["DemandKey2"]
      self.DemandKey3:str = obj["DemandKey3"]
      self.OrderNumLineRel:str = obj["OrderNumLineRel"]
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocSerialRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the allocation is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity allocated is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is allocated.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is allocated.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is allocated.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is allocated.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is allocated.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is allocated.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is allocated.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is allocated.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.DimCode:str = obj["DimCode"]
      """  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  """  
      self.SerialNum:str = obj["SerialNum"]
      """  The allocated Serial Number.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema Name of the related row.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table Name of the related row.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID of the related row.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      self.NewAllocatedQty:int = obj["NewAllocatedQty"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.Unallocate:bool = obj["Unallocate"]
      self.Allocate:bool = obj["Allocate"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranNum:int = obj["TranNum"]
      """  Part Allocation Transaction Identifier.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the allocation is for.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity allocated is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is allocated.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is allocated.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is allocated.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is allocated.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is allocated.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is allocated.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is allocated.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is allocated.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.DimCode:str = obj["DimCode"]
      """  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  """  
      self.WaveNum:int = obj["WaveNum"]
      """  Wave Number.  """  
      self.WaveDesc:str = obj["WaveDesc"]
      """  Wave Description.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Part Allocation Template Identifier.  """  
      self.AllocType:str = obj["AllocType"]
      """  Allocation Type.  Valid values:  Order or Wave.  """  
      self.DemandType:str = obj["DemandType"]
      """  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SearchSort:str = obj["SearchSort"]
      """  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.BinNumFirstOption:str = obj["BinNumFirstOption"]
      """  The first option for the bin from which to select inventory within the warehouse.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  """  
      self.CrossDocking:bool = obj["CrossDocking"]
      """  True if Cross-Docking is enabled.  """  
      self.MultiplePartsPerBin:bool = obj["MultiplePartsPerBin"]
      """  True if Multiple Parts Per Bin is allowed.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.BinNumProductionIn:str = obj["BinNumProductionIn"]
      """  The user defined Production In bin number within the warehouse.  """  
      self.ForwardStageGroup:str = obj["ForwardStageGroup"]
      """  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type.  Valid values:  Standard, Managed or Both.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WhseDestWarehouseCode:str = obj["WhseDestWarehouseCode"]
      """  Warehouse Destination for the allocated qty.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AddHoc:bool = obj["AddHoc"]
      self.Replenishable:bool = obj["Replenishable"]
      self.WaveRecordCountAfter:int = obj["WaveRecordCountAfter"]
      self.WaveRecordCountBefore:int = obj["WaveRecordCountBefore"]
      self.WarehouseCodeProductionIn:str = obj["WarehouseCodeProductionIn"]
      self.UseDemandWhseOnly:bool = obj["UseDemandWhseOnly"]
      """  Fulfill using demand warehouse only.  """  
      self.OverrideFWBUseDemandWhseOnly:bool = obj["OverrideFWBUseDemandWhseOnly"]
      """  Instructs the allocation logic to override the FWBUseDemandWhseOnly flag on the UserComp table when determining which warehouse(s) to allocate.  If true, the UseDemandWhseOnly flag on the PartAllocTran is used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AllocTempDescAllocTemplateDesc:str = obj["AllocTempDescAllocTemplateDesc"]
      self.BinDescDescription:str = obj["BinDescDescription"]
      self.BinProductionInDescDescription:str = obj["BinProductionInDescDescription"]
      self.ForwardStageZoneDescZoneDesc:str = obj["ForwardStageZoneDescZoneDesc"]
      self.WarehseDescDescription:str = obj["WarehseDescDescription"]
      self.WarehseDestDescDescription:str = obj["WarehseDestDescDescription"]
      self.WhseGrpDescWhseGroupDesc:str = obj["WhseGrpDescWhseGroupDesc"]
      self.WorkStationDescDescription:str = obj["WorkStationDescDescription"]
      self.ZoneDescZoneDesc:str = obj["ZoneDescZoneDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SlimOrderAllocRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.DemandType:str = obj["DemandType"]
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      self.FulfillmentSeq:int = obj["FulfillmentSeq"]
      self.JobNum:str = obj["JobNum"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.ReservePriorityOverride:int = obj["ReservePriorityOverride"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SlimOrderAllocTableset:
   def __init__(self, obj):
      self.SlimOrderAlloc:list[Erp_Tablesets_SlimOrderAllocRow] = obj["SlimOrderAlloc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseTeamEmpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseTeamEmpListTableset:
   def __init__(self, obj):
      self.WhseTeamEmpList:list[Erp_Tablesets_WhseTeamEmpListRow] = obj["WhseTeamEmpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetCalcPref_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCalcFulfillOnSearch:bool = obj["opCalcFulfillOnSearch"]
      pass

      """  output parameters  """  

class GetFWBFulfillFromDemandWhseOnly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFWBFulfillFromDemandWhseOnly:bool = obj["opFWBFulfillFromDemandWhseOnly"]
      pass

      """  output parameters  """  

class GetFWBLimitedRefresh_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFWBLimitedRefresh:bool = obj["opFWBLimitedRefresh"]
      pass

      """  output parameters  """  

class GetListAdvanced_input:
   """ Required : 
   i_CustId
   i_GroupCode
   i_ReservePri
   i_FromDate
   i_ToDate
   i_StartOrder
   i_EndOrder
   i_PONum
   i_PartNum
   i_DoNotShipBefore
   i_ShipVia
   i_SortBy
   i_StartingAt
   i_Order
   i_Job
   i_Transfer
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.i_CustId:str = obj["i_CustId"]
      """  Customer ID associated with the release  """  
      self.i_GroupCode:str = obj["i_GroupCode"]
      """  Customer Group Code associated with the release  """  
      self.i_ReservePri:str = obj["i_ReservePri"]
      """  Reservation Priority Code associated with the release  """  
      self.i_FromDate:str = obj["i_FromDate"]
      """  Earliest Ship Date  """  
      self.i_ToDate:str = obj["i_ToDate"]
      """  Latest Ship Date  """  
      self.i_StartOrder:int = obj["i_StartOrder"]
      """  Lowest Order Number  """  
      self.i_EndOrder:int = obj["i_EndOrder"]
      """  Highest Order Number  """  
      self.i_PONum:str = obj["i_PONum"]
      """  Customer PO Number associated with the release  """  
      self.i_PartNum:str = obj["i_PartNum"]
      """  Part Number  """  
      self.i_DoNotShipBefore:str = obj["i_DoNotShipBefore"]
      """  Do Not Ship before date associated with the release  """  
      self.i_ShipVia:str = obj["i_ShipVia"]
      """  Ship Via Code  """  
      self.i_SortBy:str = obj["i_SortBy"]
      """  Sort By field  """  
      self.i_StartingAt:str = obj["i_StartingAt"]
      """  Starting At field  """  
      self.i_Order:bool = obj["i_Order"]
      """  Order filter  """  
      self.i_Job:bool = obj["i_Job"]
      """  Job filter  """  
      self.i_Transfer:bool = obj["i_Transfer"]
      """  Transfer filter  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListAdvanced_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListAndOrderAllocationGetRows_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListAndOrderAllocationGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListBasicSearch_input:
   """ Required : 
   ipPartFrom
   ipPartTo
   ipAttributeSetID
   ipWaveFrom
   ipWaveTo
   ipPlantFrom
   ipPlantTo
   ipWhseFrom
   ipWhseTo
   ipNeedByFrom
   ipNeedByTo
   ipOrderFrom
   ipOrderTo
   ipShipByFrom
   ipShipByTo
   ipDemandType
   ipSortBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipPartFrom:str = obj["ipPartFrom"]
      """  From Part  """  
      self.ipPartTo:str = obj["ipPartTo"]
      """  To Part  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipWaveFrom:str = obj["ipWaveFrom"]
      """  From Wave  """  
      self.ipWaveTo:str = obj["ipWaveTo"]
      """  To Wave  """  
      self.ipPlantFrom:str = obj["ipPlantFrom"]
      """  From Plant  """  
      self.ipPlantTo:str = obj["ipPlantTo"]
      """  To Plant  """  
      self.ipWhseFrom:str = obj["ipWhseFrom"]
      """  From Whse  """  
      self.ipWhseTo:str = obj["ipWhseTo"]
      """  To Whse  """  
      self.ipNeedByFrom:str = obj["ipNeedByFrom"]
      """  From Need By Date  """  
      self.ipNeedByTo:str = obj["ipNeedByTo"]
      """  To Need By Date  """  
      self.ipOrderFrom:str = obj["ipOrderFrom"]
      """  From Order Date  """  
      self.ipOrderTo:str = obj["ipOrderTo"]
      """  To Order Date  """  
      self.ipShipByFrom:str = obj["ipShipByFrom"]
      """  To Ship By Date  """  
      self.ipShipByTo:str = obj["ipShipByTo"]
      """  From Ship By Date  """  
      self.ipDemandType:str = obj["ipDemandType"]
      """  Demand Type  """  
      self.ipSortBy:str = obj["ipSortBy"]
      """  Sort By  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListBasicSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListFWB_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListFWB_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocListTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfJobs_input:
   """ Required : 
   whereClausePartDtl
   whereClauseJobMtl
   whereClauseJobHead
   whereClausePartAlloc
   whereClauseWaveOrder
   i_SortByOrder
   pageSize
   absolutePage
   NO_COMPANY
   """  
   def __init__(self, obj):
      self.whereClausePartDtl:str = obj["whereClausePartDtl"]
      """  PartDtl where condition without the where word  """  
      self.whereClauseJobMtl:str = obj["whereClauseJobMtl"]
      """  JobMtl where condition without the where word  """  
      self.whereClauseJobHead:str = obj["whereClauseJobHead"]
      """  JobHead where condition without the where word  """  
      self.whereClausePartAlloc:str = obj["whereClausePartAlloc"]
      """  PartAlloc where condition without the where word  """  
      self.whereClauseWaveOrder:str = obj["whereClauseWaveOrder"]
      """  WaveOrder where condition without the where word  """  
      self.i_SortByOrder:str = obj["i_SortByOrder"]
      """  Sort condition WITH the by word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      self.NO_COMPANY:str = obj["NO_COMPANY"]
      """  NO_COMPANY  """  
      pass

class GetListOfJobs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfOrders_input:
   """ Required : 
   waveWhereClause
   orderHedWhereClause
   orderDtlWhereClause
   orderRelWhereClause
   customerWhereClause
   partAllocWhereClause
   countryWhereClause
   shipToWhereClause
   creditHoldClause
   i_SortByOrder
   i_SortByWarehouse
   i_SortByAllocation
   pageSize
   absolutePage
   NO_COMPANY
   """  
   def __init__(self, obj):
      self.waveWhereClause:str = obj["waveWhereClause"]
      """  Order Head where clause  """  
      self.orderHedWhereClause:str = obj["orderHedWhereClause"]
      """  Order Head where clause  """  
      self.orderDtlWhereClause:str = obj["orderDtlWhereClause"]
      """  Order Dtl where clause  """  
      self.orderRelWhereClause:str = obj["orderRelWhereClause"]
      """  Order Release where clause  """  
      self.customerWhereClause:str = obj["customerWhereClause"]
      """  Customer where clause  """  
      self.partAllocWhereClause:str = obj["partAllocWhereClause"]
      """  PartAlloc where clause  """  
      self.countryWhereClause:str = obj["countryWhereClause"]
      """  Country where clause  """  
      self.shipToWhereClause:str = obj["shipToWhereClause"]
      """  ShipTo where clause  """  
      self.creditHoldClause:str = obj["creditHoldClause"]
      """  Credit Hold filter clause  """  
      self.i_SortByOrder:str = obj["i_SortByOrder"]
      """  Sort By Order field  """  
      self.i_SortByWarehouse:str = obj["i_SortByWarehouse"]
      """  Sort By WarehouseCode  """  
      self.i_SortByAllocation:str = obj["i_SortByAllocation"]
      """  Sort By Allocated  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      self.NO_COMPANY:str = obj["NO_COMPANY"]
      """  NO_COMPANY  """  
      pass

class GetListOfOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfTransferOrders_input:
   """ Required : 
   whereClausePartDtl
   whereClauseTFOrdDtl
   whereClauseTFOrdHed
   whereClausePartAlloc
   whereClauseWaveOrder
   i_SortByOrder
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartDtl:str = obj["whereClausePartDtl"]
      """  PartDtl where Clause  """  
      self.whereClauseTFOrdDtl:str = obj["whereClauseTFOrdDtl"]
      """  TFOrdDtl where Clause  """  
      self.whereClauseTFOrdHed:str = obj["whereClauseTFOrdHed"]
      """  TFOrdHed where Clause  """  
      self.whereClausePartAlloc:str = obj["whereClausePartAlloc"]
      """  PartAlloc where Clause  """  
      self.whereClauseWaveOrder:str = obj["whereClauseWaveOrder"]
      """  WaveOrder where Clause  """  
      self.i_SortByOrder:str = obj["i_SortByOrder"]
      """  Sort By  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListOfTransferOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   NO_COMPANY
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      self.NO_COMPANY:str = obj["NO_COMPANY"]
      """  NO_COMPANY  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLotBinOnHandByWhseCodeZoneBinType_input:
   """ Required : 
   ds
   ipWarehouseCode
   ipWarehouseZone
   ipBinType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code  """  
      self.ipWarehouseZone:str = obj["ipWarehouseZone"]
      """  Warehouse Zone  """  
      self.ipBinType:str = obj["ipBinType"]
      """  Bin Type  """  
      pass

class GetLotBinOnHandByWhseCodeZoneBinType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetLotBinOnHandByWhseCode_input:
   """ Required : 
   ds
   ipWarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code  """  
      pass

class GetLotBinOnHandByWhseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetLotBinOnHand_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class GetLotBinOnHand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrderAllocFields_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRowsFromSelectedKeys_input:
   """ Required : 
   ds
   ipLastDisplaySeq
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.ipLastDisplaySeq:int = obj["ipLastDisplaySeq"]
      """  Last DisplaySeq value currently in the grid  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adapter  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adapter  """  
      pass

class GetRowsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSearchSortDefault_input:
   """ Required : 
   ipDemandType
   """  
   def __init__(self, obj):
      self.ipDemandType:str = obj["ipDemandType"]
      """  Demand Type - valid values are Order/Job/Transfer  """  
      pass

class GetSearchSortDefault_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opSearchSort:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSerialNumOnHandByWhseCodeZoneBinType_input:
   """ Required : 
   ds
   ipWarehouseCode
   ipWarehouseZone
   ipBinType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code  """  
      self.ipWarehouseZone:str = obj["ipWarehouseZone"]
      """  Warehouse Zone  """  
      self.ipBinType:str = obj["ipBinType"]
      """  Bin Type  """  
      pass

class GetSerialNumOnHandByWhseCodeZoneBinType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSerialNumOnHandByWhseCode_input:
   """ Required : 
   ds
   ipWarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code  """  
      pass

class GetSerialNumOnHandByWhseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSerialNumOnHand_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class GetSerialNumOnHand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSubmitOptionsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cSubmitOptionsList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetWarehouseInfo_input:
   """ Required : 
   jobNum
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  The job number of a job material record  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  The assembly sequence of a job material record  """  
      self.mtlSeq:int = obj["mtlSeq"]
      """  The material sequence of a job material record  """  
      pass

class GetWarehouseInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inputWhse:str = obj["parameters"]
      self.inputBinNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetWhseTeamUserList_input:
   """ Required : 
   groupCode
   """  
   def __init__(self, obj):
      self.groupCode:str = obj["groupCode"]
      """  Warehouse Group Code.  """  
      pass

class GetWhseTeamUserList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseTeamEmpListTableset] = obj["returnObj"]
      pass

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

class JobMtlUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class JobMtlUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MassAssign_input:
   """ Required : 
   ds
   cStageWhseCode
   cStageBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cStageWhseCode:str = obj["cStageWhseCode"]
      """  Proposed staging warehouse code  """  
      self.cStageBinNum:str = obj["cStageBinNum"]
      """  Proposed staging bin number  """  
      pass

class MassAssign_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class MtlQueueUpdate_input:
   """ Required : 
   iReleaseForPickingSeq
   """  
   def __init__(self, obj):
      self.iReleaseForPickingSeq:int = obj["iReleaseForPickingSeq"]
      """  This Release for Pickings Seq  """  
      pass

class MtlQueueUpdate_output:
   def __init__(self, obj):
      pass

class OnChangeWaveNum_input:
   """ Required : 
   newWaveNum
   ds
   """  
   def __init__(self, obj):
      self.newWaveNum:int = obj["newWaveNum"]
      """  Wave.WaveNum  """  
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class OnChangeWaveNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OneDemandType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class OneDemandType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.o_ErrorText:str = obj["parameters"]
      self.o_DemandType:str = obj["parameters"]
      pass

      """  output parameters  """  

class OrderAllocSupplyUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class OrderAllocSupplyUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OrderAllocationGetRows_input:
   """ Required : 
   ds
   ipLastDisplaySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocListTableset] = obj["ds"]
      self.ipLastDisplaySeq:int = obj["ipLastDisplaySeq"]
      """  Last DisplaySeq value currently in the grid  """  
      pass

class OrderAllocationGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocTableset] = obj["returnObj"]
      pass

class OrderRelUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class OrderRelUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecalculateWithSorting_input:
   """ Required : 
   ds
   sortColumn
   sortDirection
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.sortColumn:str = obj["sortColumn"]
      """  Column to sort  """  
      self.sortDirection:str = obj["sortDirection"]
      """  Sort Direction asc/desc  """  
      pass

class RecalculateWithSorting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Recalculate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class Recalculate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshSelectedRows_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class RefreshSelectedRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SelectForProcessing_input:
   """ Required : 
   ds
   cCountry
   cShipVia
   dEndDate
   cCustID
   cPartNum
   lAllDates
   dPctFillable
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cCountry:str = obj["cCountry"]
      """  Country code  """  
      self.cShipVia:str = obj["cShipVia"]
      """  Ship Via code  """  
      self.dEndDate:str = obj["dEndDate"]
      """  The end date  """  
      self.cCustID:str = obj["cCustID"]
      """  The customer id  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The part number  """  
      self.lAllDates:bool = obj["lAllDates"]
      """  Indicates if all dates should considered for the allocate process  """  
      self.dPctFillable:int = obj["dPctFillable"]
      """  Percent Fillable  """  
      pass

class SelectForProcessing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetCalcPref_input:
   """ Required : 
   ipCalcFulfillOnSearch
   """  
   def __init__(self, obj):
      self.ipCalcFulfillOnSearch:bool = obj["ipCalcFulfillOnSearch"]
      pass

class SetCalcPref_output:
   def __init__(self, obj):
      pass

class SetFWBFulfillFromDemandWhseOnly_input:
   """ Required : 
   ipFWBFulfillFromDemandWhseOnly
   """  
   def __init__(self, obj):
      self.ipFWBFulfillFromDemandWhseOnly:bool = obj["ipFWBFulfillFromDemandWhseOnly"]
      pass

class SetFWBFulfillFromDemandWhseOnly_output:
   def __init__(self, obj):
      pass

class SetFWBLimitedRefresh_input:
   """ Required : 
   ipFWBLimitedRefresh
   """  
   def __init__(self, obj):
      self.ipFWBLimitedRefresh:bool = obj["ipFWBLimitedRefresh"]
      pass

class SetFWBLimitedRefresh_output:
   def __init__(self, obj):
      pass

class SubmitForPicking_input:
   """ Required : 
   ds
   iNumDays
   dNeedByDate
   lUseSpecifiedDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.iNumDays:int = obj["iNumDays"]
      """  Number of days prior to ship by date  """  
      self.dNeedByDate:str = obj["dNeedByDate"]
      """  Specific need by date  """  
      self.lUseSpecifiedDate:bool = obj["lUseSpecifiedDate"]
      """  Use the specific date passed in  """  
      pass

class SubmitForPicking_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      self.iReleaseForPickingSeq:int = obj["parameters"]
      self.lReleased:bool = obj["lReleased"]
      pass

      """  output parameters  """  

class TFOrdDtlUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class TFOrdDtlUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnallocateAndReserve_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class UnallocateAndReserve_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class UnallocateAndUnreserve_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class UnallocateAndUnreserve_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class Unreserve_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      pass

class Unreserve_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderAllocTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class callGetListBasicSearch_input:
   """ Required : 
   ipPartFrom
   ipPartTo
   ipAttributeSetID
   ipWaveFrom
   ipWaveTo
   ipPlantFrom
   ipPlantTo
   ipWhseFrom
   ipWhseTo
   ipNeedByFrom
   ipNeedByTo
   ipOrderFrom
   ipOrderTo
   ipShipByFrom
   ipShipByTo
   ipDTOrders
   ipDTTransfer
   ipDTJob
   ipDTReserved
   ipDTAllocated
   ipDTPicking
   ipDTPicked
   ipSortBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipPartFrom:str = obj["ipPartFrom"]
      """  From Part  """  
      self.ipPartTo:str = obj["ipPartTo"]
      """  To Part  """  
      self.ipAttributeSetID:str = obj["ipAttributeSetID"]
      self.ipWaveFrom:str = obj["ipWaveFrom"]
      """  From Wave  """  
      self.ipWaveTo:str = obj["ipWaveTo"]
      """  To Wave  """  
      self.ipPlantFrom:str = obj["ipPlantFrom"]
      """  From Plant  """  
      self.ipPlantTo:str = obj["ipPlantTo"]
      """  To Plant  """  
      self.ipWhseFrom:str = obj["ipWhseFrom"]
      """  From Whse  """  
      self.ipWhseTo:str = obj["ipWhseTo"]
      """  To Whse  """  
      self.ipNeedByFrom:str = obj["ipNeedByFrom"]
      """  From Need By Date  """  
      self.ipNeedByTo:str = obj["ipNeedByTo"]
      """  To Need By Date  """  
      self.ipOrderFrom:str = obj["ipOrderFrom"]
      """  From Order Date  """  
      self.ipOrderTo:str = obj["ipOrderTo"]
      """  To Order Date  """  
      self.ipShipByFrom:str = obj["ipShipByFrom"]
      """  To Ship By Date  """  
      self.ipShipByTo:str = obj["ipShipByTo"]
      """  From Ship By Date  """  
      self.ipDTOrders:str = obj["ipDTOrders"]
      """  Sales Orders selected value  """  
      self.ipDTTransfer:str = obj["ipDTTransfer"]
      """  Transfer Orders selected value  """  
      self.ipDTJob:str = obj["ipDTJob"]
      """  Jobs selected value  """  
      self.ipDTReserved:str = obj["ipDTReserved"]
      """  Reserved selected value  """  
      self.ipDTAllocated:str = obj["ipDTAllocated"]
      """  Allocated selected value  """  
      self.ipDTPicking:str = obj["ipDTPicking"]
      """  InPicking selected value  """  
      self.ipDTPicked:str = obj["ipDTPicked"]
      """  Picked selected value  """  
      self.ipSortBy:str = obj["ipSortBy"]
      """  Sort By  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class callGetListBasicSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class callGetListOfJobs_input:
   """ Required : 
   ipWaveFrom
   ipWaveTo
   ipJobNumFrom
   ipJobNumTo
   ipJobTypeFrom
   ipJobTypeTo
   ipWhseFrom
   ipWhseTo
   ipRequestedFrom
   ipRequestedTo
   ipRequiredFrom
   ipRequiredTo
   ipScheduledFrom
   ipScheduledTo
   ipSchedCodeFrom
   ipSchedCodeTo
   ipTeamFrom
   ipTeamTo
   ipPlannerFrom
   ipPlannerTo
   ipGroupFrom
   ipGroupTo
   ipProjIDFrom
   ipProjIDTo
   ipCustomerIDFrom
   ipCustomerIDTo
   ipPartFrom
   ipPartTo
   ipAttributeSetID
   ipReserved
   ipAllocated
   ipPicking
   ipPicked
   ipEngineered
   ipReleased
   ipComplete
   ipSortJobNum
   ipSortReqDate
   ipSortJobType
   ipSortPlant
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipWaveFrom:str = obj["ipWaveFrom"]
      self.ipWaveTo:str = obj["ipWaveTo"]
      self.ipJobNumFrom:str = obj["ipJobNumFrom"]
      self.ipJobNumTo:str = obj["ipJobNumTo"]
      self.ipJobTypeFrom:str = obj["ipJobTypeFrom"]
      self.ipJobTypeTo:str = obj["ipJobTypeTo"]
      self.ipWhseFrom:str = obj["ipWhseFrom"]
      self.ipWhseTo:str = obj["ipWhseTo"]
      self.ipRequestedFrom:str = obj["ipRequestedFrom"]
      self.ipRequestedTo:str = obj["ipRequestedTo"]
      self.ipRequiredFrom:str = obj["ipRequiredFrom"]
      self.ipRequiredTo:str = obj["ipRequiredTo"]
      self.ipScheduledFrom:str = obj["ipScheduledFrom"]
      self.ipScheduledTo:str = obj["ipScheduledTo"]
      self.ipSchedCodeFrom:str = obj["ipSchedCodeFrom"]
      self.ipSchedCodeTo:str = obj["ipSchedCodeTo"]
      self.ipTeamFrom:str = obj["ipTeamFrom"]
      self.ipTeamTo:str = obj["ipTeamTo"]
      self.ipPlannerFrom:str = obj["ipPlannerFrom"]
      self.ipPlannerTo:str = obj["ipPlannerTo"]
      self.ipGroupFrom:str = obj["ipGroupFrom"]
      self.ipGroupTo:str = obj["ipGroupTo"]
      self.ipProjIDFrom:str = obj["ipProjIDFrom"]
      self.ipProjIDTo:str = obj["ipProjIDTo"]
      self.ipCustomerIDFrom:str = obj["ipCustomerIDFrom"]
      self.ipCustomerIDTo:str = obj["ipCustomerIDTo"]
      self.ipPartFrom:str = obj["ipPartFrom"]
      self.ipPartTo:str = obj["ipPartTo"]
      self.ipAttributeSetID:str = obj["ipAttributeSetID"]
      self.ipReserved:str = obj["ipReserved"]
      self.ipAllocated:str = obj["ipAllocated"]
      self.ipPicking:str = obj["ipPicking"]
      self.ipPicked:str = obj["ipPicked"]
      self.ipEngineered:str = obj["ipEngineered"]
      self.ipReleased:str = obj["ipReleased"]
      self.ipComplete:str = obj["ipComplete"]
      self.ipSortJobNum:str = obj["ipSortJobNum"]
      self.ipSortReqDate:str = obj["ipSortReqDate"]
      self.ipSortJobType:str = obj["ipSortJobType"]
      self.ipSortPlant:str = obj["ipSortPlant"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class callGetListOfJobs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class callGetListOfOrders_input:
   """ Required : 
   ipWaveFrom
   ipWaveTo
   ipOrderNumFrom
   ipOrderNumTo
   ipPriCodeFrom
   ipPriCodeTo
   ipWhseFrom
   ipWhseTo
   ipNeedByFrom
   ipNeedByTo
   ipOrderFrom
   ipOrderTo
   ipShipByFrom
   ipShipByTo
   ipCusGroupFrom
   ipCusGroupTo
   ipPartFrom
   ipPartTo
   ipAttributeSetID
   ipShipViaFrom
   ipShipViaTo
   ipShipToFrom
   ipShipToTo
   ipShipCityFrom
   ipShipCityTo
   ipShipStateFrom
   ipShipStateTo
   ipZipFrom
   ipZipTo
   ipShipCountryFrom
   ipShipCountryTo
   ipSoldToFrom
   ipSoldToTo
   ipCustPOFrom
   ipCustPOTo
   ipProjIDFrom
   ipProjIDTo
   ipReserved
   ipAllocated
   ipPicking
   ipPicked
   ipShipComp
   ipCreditHold
   ipUserHold
   ipCountSales
   ipSortOrder
   ipSortShipDate
   ipSortWhse
   ipSortAlloc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipWaveFrom:str = obj["ipWaveFrom"]
      self.ipWaveTo:str = obj["ipWaveTo"]
      self.ipOrderNumFrom:str = obj["ipOrderNumFrom"]
      self.ipOrderNumTo:str = obj["ipOrderNumTo"]
      self.ipPriCodeFrom:str = obj["ipPriCodeFrom"]
      self.ipPriCodeTo:str = obj["ipPriCodeTo"]
      self.ipWhseFrom:str = obj["ipWhseFrom"]
      self.ipWhseTo:str = obj["ipWhseTo"]
      self.ipNeedByFrom:str = obj["ipNeedByFrom"]
      self.ipNeedByTo:str = obj["ipNeedByTo"]
      self.ipOrderFrom:str = obj["ipOrderFrom"]
      self.ipOrderTo:str = obj["ipOrderTo"]
      self.ipShipByFrom:str = obj["ipShipByFrom"]
      self.ipShipByTo:str = obj["ipShipByTo"]
      self.ipCusGroupFrom:str = obj["ipCusGroupFrom"]
      self.ipCusGroupTo:str = obj["ipCusGroupTo"]
      self.ipPartFrom:str = obj["ipPartFrom"]
      self.ipPartTo:str = obj["ipPartTo"]
      self.ipAttributeSetID:str = obj["ipAttributeSetID"]
      self.ipShipViaFrom:str = obj["ipShipViaFrom"]
      self.ipShipViaTo:str = obj["ipShipViaTo"]
      self.ipShipToFrom:str = obj["ipShipToFrom"]
      self.ipShipToTo:str = obj["ipShipToTo"]
      self.ipShipCityFrom:str = obj["ipShipCityFrom"]
      self.ipShipCityTo:str = obj["ipShipCityTo"]
      self.ipShipStateFrom:str = obj["ipShipStateFrom"]
      self.ipShipStateTo:str = obj["ipShipStateTo"]
      self.ipZipFrom:str = obj["ipZipFrom"]
      self.ipZipTo:str = obj["ipZipTo"]
      self.ipShipCountryFrom:int = obj["ipShipCountryFrom"]
      self.ipShipCountryTo:int = obj["ipShipCountryTo"]
      self.ipSoldToFrom:str = obj["ipSoldToFrom"]
      self.ipSoldToTo:str = obj["ipSoldToTo"]
      self.ipCustPOFrom:str = obj["ipCustPOFrom"]
      self.ipCustPOTo:str = obj["ipCustPOTo"]
      self.ipProjIDFrom:str = obj["ipProjIDFrom"]
      self.ipProjIDTo:str = obj["ipProjIDTo"]
      self.ipReserved:str = obj["ipReserved"]
      self.ipAllocated:str = obj["ipAllocated"]
      self.ipPicking:str = obj["ipPicking"]
      self.ipPicked:str = obj["ipPicked"]
      self.ipShipComp:str = obj["ipShipComp"]
      self.ipCreditHold:str = obj["ipCreditHold"]
      self.ipUserHold:str = obj["ipUserHold"]
      self.ipCountSales:str = obj["ipCountSales"]
      self.ipSortOrder:str = obj["ipSortOrder"]
      self.ipSortShipDate:str = obj["ipSortShipDate"]
      self.ipSortWhse:str = obj["ipSortWhse"]
      self.ipSortAlloc:str = obj["ipSortAlloc"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class callGetListOfOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class callGetListOfTransferOrders_input:
   """ Required : 
   ipWaveFrom
   ipWaveTo
   ipTransferFrom
   ipTransferTo
   ipLineStatus
   ipLineOpen
   ipPlantFrom
   ipPlantTo
   ipWhseFrom
   ipWhseTo
   ipTransOrderFrom
   ipTransOrderTo
   ipNeedFrom
   ipNeedTo
   ipShipFrom
   ipShipTo
   ipPartFrom
   ipPartTo
   ipAttributeSetID
   ipShipViaFrom
   ipShipViaTo
   ipReserved
   ipAllocated
   ipPicking
   ipPicked
   ipSortOrder
   ipShipBy
   ipToPlant
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipWaveFrom:str = obj["ipWaveFrom"]
      self.ipWaveTo:str = obj["ipWaveTo"]
      self.ipTransferFrom:str = obj["ipTransferFrom"]
      self.ipTransferTo:str = obj["ipTransferTo"]
      self.ipLineStatus:str = obj["ipLineStatus"]
      self.ipLineOpen:str = obj["ipLineOpen"]
      self.ipPlantFrom:str = obj["ipPlantFrom"]
      self.ipPlantTo:str = obj["ipPlantTo"]
      self.ipWhseFrom:str = obj["ipWhseFrom"]
      self.ipWhseTo:str = obj["ipWhseTo"]
      self.ipTransOrderFrom:str = obj["ipTransOrderFrom"]
      self.ipTransOrderTo:str = obj["ipTransOrderTo"]
      self.ipNeedFrom:str = obj["ipNeedFrom"]
      self.ipNeedTo:str = obj["ipNeedTo"]
      self.ipShipFrom:str = obj["ipShipFrom"]
      self.ipShipTo:str = obj["ipShipTo"]
      self.ipPartFrom:str = obj["ipPartFrom"]
      self.ipPartTo:str = obj["ipPartTo"]
      self.ipAttributeSetID:str = obj["ipAttributeSetID"]
      self.ipShipViaFrom:str = obj["ipShipViaFrom"]
      self.ipShipViaTo:str = obj["ipShipViaTo"]
      self.ipReserved:str = obj["ipReserved"]
      self.ipAllocated:str = obj["ipAllocated"]
      self.ipPicking:str = obj["ipPicking"]
      self.ipPicked:str = obj["ipPicked"]
      self.ipSortOrder:str = obj["ipSortOrder"]
      self.ipShipBy:str = obj["ipShipBy"]
      self.ipToPlant:str = obj["ipToPlant"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class callGetListOfTransferOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderAllocListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

