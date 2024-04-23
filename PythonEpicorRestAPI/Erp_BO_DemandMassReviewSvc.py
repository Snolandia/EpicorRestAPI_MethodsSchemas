import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandMassReviewSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CloseAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseAll
   Description: Purpose:
Parameters:  none
Notes:
<param>The Demand Mass Review Data Set</param>
   OperationID: CloseAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseAllPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseAllPart
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseAllPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseAllPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAllPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseDemand
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseRejectedDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseRejectedDemand
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseRejectedDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseRejectedDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseRejectedDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseWorkList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseWorkList
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseWorkList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseWorkList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseWorkList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteDemand
   Description: Delete the schedules related to the selected Part/Demand. Demand Mass Review
summarize demands, on that case will we be deleting all schedules that were
included on that selected record. If a schedule is selected for another
Group different than the current, we'll check if it is not locked and if not
we can delete the schedule.
   OperationID: DeleteDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteGroup
   OperationID: DeleteGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDemandMassReview(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDemandMassReview
   Description: Call this method when the user selects parts or demands to review.  This
method populates the Epicor.Mfg.BO.DemandMassReviewDataSet dataset for
criteria selected.
   OperationID: GetDemandMassReview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDemandMassReview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandMassReview_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMassReviewDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMassReviewDtl
   Description: Call this method to get the demand details for a part when a different part
is selected.
   OperationID: GetMassReviewDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMassReviewDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassReviewDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchAllForDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchAllForDemand
   Description: This method will perform the default matching of Demand Schedules
to Order Releases for a demand.
   OperationID: MatchAllForDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchAllForDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchAllForDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchAllForPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchAllForPart
   Description: This method will perform the default matching of Demand Schedules
to Order Releases for a part.
   OperationID: MatchAllForPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchAllForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchAllForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUOM
   Description: Updates the On Hand Quantity according to the UOM
method populates the Epicor.Mfg.BO.DemandMassReviewDataSet dataset for
criteria selected.
   OperationID: OnChangeUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessingSelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessingSelectAll
   Description: This method will set all demands that have not been posted to be ready for processing.
   OperationID: ProcessingSelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessingSelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessingSelectAllForPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessingSelectAllForPart
   Description: This method will mark all demands for a part to be ready for processing.
   OperationID: ProcessingSelectAllForPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessingSelectAllForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectAllForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessingSelectByDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessingSelectByDemand
   Description: This method will mark a demand as be ready for processing.
   OperationID: ProcessingSelectByDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessingSelectByDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectByDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessingSelectWorkList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessingSelectWorkList
   Description: This method will mark all demands for the work list to be ready for processing.
   OperationID: ProcessingSelectWorkList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessingSelectWorkList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectWorkList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RejectAllForDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RejectAllForDemand
   Description: This method will mark a demand as rejected.
   OperationID: RejectAllForDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectAllForDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectAllForDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RejectAllForPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RejectAllForPart
   Description: This method will mark all demands for a part as rejected.
   OperationID: RejectAllForPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RejectAllForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectAllForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchAll
   Description: Unmatch all the demand entries previously loaded
   OperationID: UnmatchAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CloseAllPart_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class CloseAllPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class CloseAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseDemand_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class CloseDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseRejectedDemand_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class CloseRejectedDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseWorkList_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class CloseWorkList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteDemand_input:
   """ Required : 
   ds
   ipGroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      pass

class DeleteDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteGroup_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      pass

class DeleteGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DemandMassInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMassInputsTableset:
   def __init__(self, obj):
      self.DemandMassInputs:list[Erp_Tablesets_DemandMassInputsRow] = obj["DemandMassInputs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandMassReviewDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PrimaryField:str = obj["PrimaryField"]
      self.PrimaryFieldDtl:str = obj["PrimaryFieldDtl"]
      self.CustID:str = obj["CustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandContract:str = obj["DemandContract"]
      self.DemandPONum:str = obj["DemandPONum"]
      self.PartNum:str = obj["PartNum"]
      self.PartDesc:str = obj["PartDesc"]
      self.MDPV:int = obj["MDPV"]
      """  .  """  
      self.PartOnHandQty:int = obj["PartOnHandQty"]
      self.PartAvailableQty:int = obj["PartAvailableQty"]
      self.BalanceDifference:int = obj["BalanceDifference"]
      self.CostQtyDifference:int = obj["CostQtyDifference"]
      self.CurBalance:int = obj["CurBalance"]
      self.CurDemandQty:int = obj["CurDemandQty"]
      self.ProposedBalance:int = obj["ProposedBalance"]
      self.ProposedDemandQty:int = obj["ProposedDemandQty"]
      self.QuantityDifference:int = obj["QuantityDifference"]
      self.SelectForProcess:bool = obj["SelectForProcess"]
      self.Reject:bool = obj["Reject"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.RecordType:str = obj["RecordType"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.ContractUnitPrice:int = obj["ContractUnitPrice"]
      self.DemandUnitPrice:int = obj["DemandUnitPrice"]
      self.CurDemandQtyUOM:str = obj["CurDemandQtyUOM"]
      """  Current Demand UOM  """  
      self.ProposedDemandQtyUOM:str = obj["ProposedDemandQtyUOM"]
      """  Proposed Demand UOM  """  
      self.Closed:bool = obj["Closed"]
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      self.DemandType:str = obj["DemandType"]
      self.GroupID:str = obj["GroupID"]
      """  All Demand Reviews belong to a group until the group is posted. The GroupID is assigned by the user.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMassReviewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PrimaryField:str = obj["PrimaryField"]
      """  The primary field for this table.  It will have either the Part Number or a concatenated string of demand contract name and po.  """  
      self.RecordType:str = obj["RecordType"]
      """  The type of record this is.  Options are (P)art or (C)ontract/PO.  """  
      self.CustID:str = obj["CustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandPONum:str = obj["DemandPONum"]
      self.PartNum:str = obj["PartNum"]
      self.MDPV:int = obj["MDPV"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.DemandContract:str = obj["DemandContract"]
      self.SelectForProcess:bool = obj["SelectForProcess"]
      self.Reject:bool = obj["Reject"]
      self.Description:str = obj["Description"]
      self.UOM:str = obj["UOM"]
      """  Part UOM  """  
      self.AvailableQtyUOM:str = obj["AvailableQtyUOM"]
      """  Available Quantity UOM  """  
      self.MDPVUOM:str = obj["MDPVUOM"]
      """  MDPV UOM  """  
      self.OnHandQtyUOM:str = obj["OnHandQtyUOM"]
      """  On Hand Quantity UOM  """  
      self.Closed:bool = obj["Closed"]
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      self.GroupID:str = obj["GroupID"]
      self.TrackUOM:bool = obj["TrackUOM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMassReviewTableset:
   def __init__(self, obj):
      self.DemandMassReview:list[Erp_Tablesets_DemandMassReviewRow] = obj["DemandMassReview"]
      self.DemandMassReviewDtl:list[Erp_Tablesets_DemandMassReviewDtlRow] = obj["DemandMassReviewDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetDemandMassReview_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.ds:list[Erp_Tablesets_DemandMassInputsTableset] = obj["ds"]
      pass

class GetDemandMassReview_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandMassReviewTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassInputsTableset] = obj["ds"]
      self.cOutputMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetMassReviewDtl_input:
   """ Required : 
   ipGroupID
   cPrimaryField
   lFirm
   lUnfirm
   lForecast
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.cPrimaryField:str = obj["cPrimaryField"]
      """  The primary field value of DemandMassReview  """  
      self.lFirm:bool = obj["lFirm"]
      """  Include Firm Demand Schedules?  """  
      self.lUnfirm:bool = obj["lUnfirm"]
      """  Include Unfirm Demand Schedules?  """  
      self.lForecast:bool = obj["lForecast"]
      """  Include Forecast Demand Schedules?  """  
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class GetMassReviewDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
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

class MatchAllForDemand_input:
   """ Required : 
   ipGroupID
   iDemandContractNum
   iDemandHeadSeq
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Contract Number to process  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Head identifier to process  """  
      pass

class MatchAllForDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      self.lMatched:bool = obj["lMatched"]
      pass

      """  output parameters  """  

class MatchAllForPart_input:
   """ Required : 
   ipGroupID
   cPartNum
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to process  """  
      pass

class MatchAllForPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeUOM_input:
   """ Required : 
   cPrimaryField
   ds
   """  
   def __init__(self, obj):
      self.cPrimaryField:str = obj["cPrimaryField"]
      """  The primary field value of DemandMassReview  """  
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class OnChangeUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessingSelectAllForPart_input:
   """ Required : 
   ipGroupID
   cPartNum
   cSelectType
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to process  """  
      self.cSelectType:str = obj["cSelectType"]
      """  (S)elect or (U)nselect  """  
      pass

class ProcessingSelectAllForPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessingSelectAll_input:
   """ Required : 
   ipGroupID
   cSelectType
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.cSelectType:str = obj["cSelectType"]
      """  (S)elect or (U)nselect all  """  
      pass

class ProcessingSelectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessingSelectByDemand_input:
   """ Required : 
   ipGroupID
   iDemandContractNum
   iDemandHeadSeq
   cSelectType
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Contract Number to process  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Head identifier to process  """  
      self.cSelectType:str = obj["cSelectType"]
      """  (S)elect or (U)nselect  """  
      pass

class ProcessingSelectByDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessingSelectWorkList_input:
   """ Required : 
   ds
   ipGroupID
   cSelectType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassInputsTableset] = obj["ds"]
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.cSelectType:str = obj["cSelectType"]
      """  (S)elect or (U)nselect  """  
      pass

class ProcessingSelectWorkList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassInputsTableset] = obj["ds"]
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class RejectAllForDemand_input:
   """ Required : 
   ipGroupID
   iDemandContractNum
   iDemandHeadSeq
   cRejectType
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Contract Number to process  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The Demand Head identifier to process  """  
      self.cRejectType:str = obj["cRejectType"]
      """  (R)eject or (U)nreject  """  
      pass

class RejectAllForDemand_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class RejectAllForPart_input:
   """ Required : 
   ipGroupID
   cPartNum
   cRejectType
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Demand Mass Review Current Group.  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to process  """  
      self.cRejectType:str = obj["cRejectType"]
      """  (R)eject or (U)nreject  """  
      pass

class RejectAllForPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UnmatchAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      pass

class UnmatchAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandMassReviewTableset] = obj["ds"]
      self.cOutputMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

