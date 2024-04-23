import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ExtPRPayClassSvc
# Description: BO to register the different Payroll Pay Classes to be used when calculating the hours to be exported to the External Vendor Payroll System
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRPayClasses(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRPayClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRPayClasses
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRPayClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/ExtPRPayClasses",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRPayClasses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRPayClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRPayClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRPayClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/ExtPRPayClasses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRPayClasses_Company_PayClassID(Company, PayClassID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRPayClass item
   Description: Calls GetByID to retrieve the ExtPRPayClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRPayClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayClassID: Desc: PayClassID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRPayClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/ExtPRPayClasses(" + Company + "," + PayClassID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRPayClasses_Company_PayClassID(Company, PayClassID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRPayClass for the service
   Description: Calls UpdateExt to update ExtPRPayClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRPayClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayClassID: Desc: PayClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRPayClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/ExtPRPayClasses(" + Company + "," + PayClassID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRPayClasses_Company_PayClassID(Company, PayClassID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRPayClass item
   Description: Call UpdateExt to delete ExtPRPayClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRPayClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PayClassID: Desc: PayClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/ExtPRPayClasses(" + Company + "," + PayClassID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRPayClassListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtPRPayClass, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
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
   params += "whereClauseExtPRPayClass=" + whereClauseExtPRPayClass
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(payClassID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "payClassID=" + payClassID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
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

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRPayClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRPayClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRPayClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRPayClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRPayClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtPRPayClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRPayClassListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRPayClassListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRPayClassRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRPayClassRow] = obj["value"]
      pass

class Erp_Tablesets_ExtPRPayClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayClassID:str = obj["PayClassID"]
      """  Payroll Class ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRPayClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayClassID:str = obj["PayClassID"]
      """  Payroll Class ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.HolidayOT:bool = obj["HolidayOT"]
      """  Include Holiday Hours for O/T Calculation  """  
      self.VacOT:bool = obj["VacOT"]
      """  Include Vacation Hours for O/T Calculation  """  
      self.SickOT:bool = obj["SickOT"]
      """  Include Sick  Hours for O/T Calculation  """  
      self.PTO:bool = obj["PTO"]
      """  Include Personal Hours for O/T Calculation  """  
      self.OTPerDay:int = obj["OTPerDay"]
      """  Over Time Hours Per Day  """  
      self.OTPerWeek:int = obj["OTPerWeek"]
      """  Over Time Hours Per Week  """  
      self.DTPerDay:int = obj["DTPerDay"]
      """  Double Time Hours Per Day  """  
      self.DTPerWeek:int = obj["DTPerWeek"]
      """  Double Time Hours Per Week  """  
      self.PTMonFri:str = obj["PTMonFri"]
      """  Pay Type to be used Monday through Friday  """  
      self.PTSat:str = obj["PTSat"]
      """  Pay Type to be used Saturdays  """  
      self.PTSun:str = obj["PTSun"]
      """  Pay Type to be used Sundays  """  
      self.PTHoliday:str = obj["PTHoliday"]
      """  Pay Type to be used for Holidays  """  
      self.HolExemptDays:int = obj["HolExemptDays"]
      """  Number of calendar days needed to wait prior to holiday dates to be paid to employee  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PTHolLabor:str = obj["PTHolLabor"]
      """  Pay Type to be used for labor hours entered on a Holiday.  """  
      self.ExtPRPerDayAllFreq:bool = obj["ExtPRPerDayAllFreq"]
      """  ExtPRPerDayAllFreq  """  
      self.EarlyClockInAllowance:int = obj["EarlyClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock in times are to be adjusted forward to the shift start time.  If clock in time falls within the  time range of (Shift Start - Allowance) to Shift Start then the clock in time will set to Shift Start time.  """  
      self.EarlyClockOutAllowance:int = obj["EarlyClockOutAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock out times are to be adjusted forward to the shift end time.  If clock out time falls within the  time range of (Shift End - Allowance) to Shift End  then the clock out time will set to Shift end.  """  
      self.LateClockInAllowance:int = obj["LateClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which late clock in times are to be adjusted backwards to the shift start time.  If clock in time falls within the  time range of Shift Start to (Shift Start + Allowance)  then the clock in time will set to Shift Start time.  """  
      self.LateClockOutAllowance:int = obj["LateClockOutAllowance"]
      """  Minutes used to determine the time frame in which late clock out times are to be adjusted backwards to the shift end time.  If clock out time falls within the  time range of Shift end to (Shift Start + Allowance) then the clock out time will set to Shift End time.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   payClassID
   """  
   def __init__(self, obj):
      self.payClassID:str = obj["payClassID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ExtPRPayClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayClassID:str = obj["PayClassID"]
      """  Payroll Class ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRPayClassListTableset:
   def __init__(self, obj):
      self.ExtPRPayClassList:list[Erp_Tablesets_ExtPRPayClassListRow] = obj["ExtPRPayClassList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtPRPayClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PayClassID:str = obj["PayClassID"]
      """  Payroll Class ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.HolidayOT:bool = obj["HolidayOT"]
      """  Include Holiday Hours for O/T Calculation  """  
      self.VacOT:bool = obj["VacOT"]
      """  Include Vacation Hours for O/T Calculation  """  
      self.SickOT:bool = obj["SickOT"]
      """  Include Sick  Hours for O/T Calculation  """  
      self.PTO:bool = obj["PTO"]
      """  Include Personal Hours for O/T Calculation  """  
      self.OTPerDay:int = obj["OTPerDay"]
      """  Over Time Hours Per Day  """  
      self.OTPerWeek:int = obj["OTPerWeek"]
      """  Over Time Hours Per Week  """  
      self.DTPerDay:int = obj["DTPerDay"]
      """  Double Time Hours Per Day  """  
      self.DTPerWeek:int = obj["DTPerWeek"]
      """  Double Time Hours Per Week  """  
      self.PTMonFri:str = obj["PTMonFri"]
      """  Pay Type to be used Monday through Friday  """  
      self.PTSat:str = obj["PTSat"]
      """  Pay Type to be used Saturdays  """  
      self.PTSun:str = obj["PTSun"]
      """  Pay Type to be used Sundays  """  
      self.PTHoliday:str = obj["PTHoliday"]
      """  Pay Type to be used for Holidays  """  
      self.HolExemptDays:int = obj["HolExemptDays"]
      """  Number of calendar days needed to wait prior to holiday dates to be paid to employee  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PTHolLabor:str = obj["PTHolLabor"]
      """  Pay Type to be used for labor hours entered on a Holiday.  """  
      self.ExtPRPerDayAllFreq:bool = obj["ExtPRPerDayAllFreq"]
      """  ExtPRPerDayAllFreq  """  
      self.EarlyClockInAllowance:int = obj["EarlyClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock in times are to be adjusted forward to the shift start time.  If clock in time falls within the  time range of (Shift Start - Allowance) to Shift Start then the clock in time will set to Shift Start time.  """  
      self.EarlyClockOutAllowance:int = obj["EarlyClockOutAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock out times are to be adjusted forward to the shift end time.  If clock out time falls within the  time range of (Shift End - Allowance) to Shift End  then the clock out time will set to Shift end.  """  
      self.LateClockInAllowance:int = obj["LateClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which late clock in times are to be adjusted backwards to the shift start time.  If clock in time falls within the  time range of Shift Start to (Shift Start + Allowance)  then the clock in time will set to Shift Start time.  """  
      self.LateClockOutAllowance:int = obj["LateClockOutAllowance"]
      """  Minutes used to determine the time frame in which late clock out times are to be adjusted backwards to the shift end time.  If clock out time falls within the  time range of Shift end to (Shift Start + Allowance) then the clock out time will set to Shift End time.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRPayClassTableset:
   def __init__(self, obj):
      self.ExtPRPayClass:list[Erp_Tablesets_ExtPRPayClassRow] = obj["ExtPRPayClass"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtExtPRPayClassTableset:
   def __init__(self, obj):
      self.ExtPRPayClass:list[Erp_Tablesets_ExtPRPayClassRow] = obj["ExtPRPayClass"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   payClassID
   """  
   def __init__(self, obj):
      self.payClassID:str = obj["payClassID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRPayClassListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExtPRPayClass_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["ds"]
      pass

class GetNewExtPRPayClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtPRPayClass
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtPRPayClass:str = obj["whereClauseExtPRPayClass"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtPRPayClassTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtPRPayClassTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtPRPayClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

