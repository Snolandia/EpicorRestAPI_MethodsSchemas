import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PCashCloseDaySvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PCashCloseDays(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashCloseDays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashCloseDays
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashBalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays",headers=creds) as resp:
           return await resp.json()

async def post_PCashCloseDays(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashCloseDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashBalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashBalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashCloseDays_Company_CashDeskID_Date(Company, CashDeskID, Date, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashCloseDay item
   Description: Calls GetByID to retrieve the PCashCloseDay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashCloseDay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param Date: Desc: Date   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashBalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays(" + Company + "," + CashDeskID + "," + Date + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashCloseDays_Company_CashDeskID_Date(Company, CashDeskID, Date, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashCloseDay for the service
   Description: Calls UpdateExt to update PCashCloseDay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashCloseDay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param Date: Desc: Date   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashBalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays(" + Company + "," + CashDeskID + "," + Date + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashCloseDays_Company_CashDeskID_Date(Company, CashDeskID, Date, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashCloseDay item
   Description: Call UpdateExt to delete PCashCloseDay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashCloseDay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param Date: Desc: Date   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays(" + Company + "," + CashDeskID + "," + Date + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashBalListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePCashBal, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePCashBal=" + whereClausePCashBal
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(cashDeskID, date, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "cashDeskID=" + cashDeskID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "date=" + date

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ClosePettyCashDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClosePettyCashDay
   Description: Close a day for a petty cash desk.
   OperationID: ClosePettyCashDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePettyCashDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePettyCashDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashBal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashBal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashBalListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashBalRow] = obj["value"]
      pass

class Erp_Tablesets_PCashBalListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashBalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Date:str = obj["Date"]
      """  A unique value. Date for which calculated Cash Desk Balances.  """  
      self.CashIssueCount:int = obj["CashIssueCount"]
      """  Number of Cash Issue Documents per day  """  
      self.CashRcptCount:int = obj["CashRcptCount"]
      """  Number of Cash Receipt Documents per day  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DayIsClosed:bool = obj["DayIsClosed"]
      """  Day is Closed  """  
      self.DocRcvCashAmt:int = obj["DocRcvCashAmt"]
      """  Total cash amount received per day  """  
      self.RcvCashAmt:int = obj["RcvCashAmt"]
      """  Total cash amount received per day  """  
      self.Rpt1RcvCashAmt:int = obj["Rpt1RcvCashAmt"]
      """  Total cash amount received per day in reporting Currency  """  
      self.Rpt2RcvCashAmt:int = obj["Rpt2RcvCashAmt"]
      """  Total cash amount received per day in reporting Currency  """  
      self.Rpt3RcvCashAmt:int = obj["Rpt3RcvCashAmt"]
      """  Total cash amount received per day in reporting Currency  """  
      self.DocRcvPayrollAmt:int = obj["DocRcvPayrollAmt"]
      """  Total cash amount received per day by payroll operations only  """  
      self.RcvPayrollAmt:int = obj["RcvPayrollAmt"]
      """  Total cash amount received per day by payroll operations only  """  
      self.Rpt1RcvPayrollAmt:int = obj["Rpt1RcvPayrollAmt"]
      """  Received Payroll Amount in reporting Currency  """  
      self.Rpt2RcvPayrollAmt:int = obj["Rpt2RcvPayrollAmt"]
      """  Received Payroll Amount in reporting Currency  """  
      self.Rpt3RcvPayrollAmt:int = obj["Rpt3RcvPayrollAmt"]
      """  Received Payroll Amount in reporting Currency  """  
      self.DocTotalRcvAmt:int = obj["DocTotalRcvAmt"]
      """  Total cash amount received per day with draft document amounts  """  
      self.RcvTotalAmt:int = obj["RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts  """  
      self.Rpt1RcvTotalAmt:int = obj["Rpt1RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts in reporting Currency  """  
      self.Rpt2RcvTotalAmt:int = obj["Rpt2RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts in reporting Currency  """  
      self.Rpt3RcvTotalAmt:int = obj["Rpt3RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts in reporting Currency.  """  
      self.DocIssCashAmt:int = obj["DocIssCashAmt"]
      """  Total cash amount Issued per day.  """  
      self.IssCashAmt:int = obj["IssCashAmt"]
      """  Total cash amount Issued per day  """  
      self.Rpt1IssCashAmt:int = obj["Rpt1IssCashAmt"]
      """  Total cash amount Issued per day in reporting Currency  """  
      self.Rpt2IssCashAmt:int = obj["Rpt2IssCashAmt"]
      """  Total cash amount Issued per day in reporting Currency  """  
      self.Rpt3IssCashAmt:int = obj["Rpt3IssCashAmt"]
      """  Total cash amount Issued per day in reporting Currency  """  
      self.DocIssPayrollAmt:int = obj["DocIssPayrollAmt"]
      """  Total cash amount Issued per day by payroll operations only  """  
      self.IssPayrollAmt:int = obj["IssPayrollAmt"]
      """  Total cash amount Issued per day by payroll operations only  """  
      self.Rpt1IssPayrollAmt:int = obj["Rpt1IssPayrollAmt"]
      """  Issued Payroll Amount in reporting Currency  """  
      self.Rpt2IssPayrollAmt:int = obj["Rpt2IssPayrollAmt"]
      """  Issued Payroll Amount in reporting Currency  """  
      self.Rpt3IssPayrollAmt:int = obj["Rpt3IssPayrollAmt"]
      """  Issued Payroll Amount in reporting Currency  """  
      self.DocIssTotalAmt:int = obj["DocIssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts  """  
      self.IssTotalAmt:int = obj["IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts  """  
      self.Rpt1IssTotalAmt:int = obj["Rpt1IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts in reporting Currency  """  
      self.Rpt2IssTotalAmt:int = obj["Rpt2IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts in reporting Currency  """  
      self.Rpt3IssTotalAmt:int = obj["Rpt3IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts in reporting Currency  """  
      self.DocDayBal:int = obj["DocDayBal"]
      """  Cash Desk Day Closing Balance  """  
      self.DayBal:int = obj["DayBal"]
      """  Cash Desk Day Closing Balance  """  
      self.Rpt1DayBal:int = obj["Rpt1DayBal"]
      """  Cash Desk Day Closing Balance in reporting Currency  """  
      self.Rpt2DayBal:int = obj["Rpt2DayBal"]
      """  Cash Desk Day Closing Balance in reporting Currency  """  
      self.Rpt3DayBal:int = obj["Rpt3DayBal"]
      """  Cash Desk Day Closing Balance in reporting Currency  """  
      self.DocPayrollDayBal:int = obj["DocPayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance  """  
      self.PayrollDayBal:int = obj["PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance  """  
      self.Rpt1PayrollDayBal:int = obj["Rpt1PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance in reporting Currency  """  
      self.Rpt2PayrollDayBal:int = obj["Rpt2PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance in reporting Currency  """  
      self.Rpt3PayrollDayBal:int = obj["Rpt3PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance in reporting Currency  """  
      self.DocDayBalWithDraft:int = obj["DocDayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  """  
      self.DayBalWithDraft:int = obj["DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  """  
      self.Rpt1DayBalWithDraft:int = obj["Rpt1DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  """  
      self.Rpt2DayBalWithDraft:int = obj["Rpt2DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  """  
      self.Rpt3DayBalWithDraft:int = obj["Rpt3DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts in reporting Currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GainLossBal:int = obj["GainLossBal"]
      """  GainLossBal  """  
      self.DocGainLossBal:int = obj["DocGainLossBal"]
      """  DocGainLossBal  """  
      self.Rpt1GainLossBal:int = obj["Rpt1GainLossBal"]
      """  Rpt1GainLossBal  """  
      self.Rpt2GainLossBal:int = obj["Rpt2GainLossBal"]
      """  Rpt2GainLossBal  """  
      self.Rpt3GainLossBal:int = obj["Rpt3GainLossBal"]
      """  Rpt3GainLossBal  """  
      self.PrintedOfficial:bool = obj["PrintedOfficial"]
      """  PrintedOfficial  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ClosePettyCashDay_input:
   """ Required : 
   cashDeskID
   dteUpto
   dtePrgDraftsBefore
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      """  Cash Desk ID.  """  
      self.dteUpto:str = obj["dteUpto"]
      """  Close Up to Date.  """  
      self.dtePrgDraftsBefore:str = obj["dtePrgDraftsBefore"]
      """  Purge Drafts Before date.  """  
      pass

class ClosePettyCashDay_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   cashDeskID
   date
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      self.date:str = obj["date"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PCashBalListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashBalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Date:str = obj["Date"]
      """  A unique value. Date for which calculated Cash Desk Balances.  """  
      self.CashIssueCount:int = obj["CashIssueCount"]
      """  Number of Cash Issue Documents per day  """  
      self.CashRcptCount:int = obj["CashRcptCount"]
      """  Number of Cash Receipt Documents per day  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DayIsClosed:bool = obj["DayIsClosed"]
      """  Day is Closed  """  
      self.DocRcvCashAmt:int = obj["DocRcvCashAmt"]
      """  Total cash amount received per day  """  
      self.RcvCashAmt:int = obj["RcvCashAmt"]
      """  Total cash amount received per day  """  
      self.Rpt1RcvCashAmt:int = obj["Rpt1RcvCashAmt"]
      """  Total cash amount received per day in reporting Currency  """  
      self.Rpt2RcvCashAmt:int = obj["Rpt2RcvCashAmt"]
      """  Total cash amount received per day in reporting Currency  """  
      self.Rpt3RcvCashAmt:int = obj["Rpt3RcvCashAmt"]
      """  Total cash amount received per day in reporting Currency  """  
      self.DocRcvPayrollAmt:int = obj["DocRcvPayrollAmt"]
      """  Total cash amount received per day by payroll operations only  """  
      self.RcvPayrollAmt:int = obj["RcvPayrollAmt"]
      """  Total cash amount received per day by payroll operations only  """  
      self.Rpt1RcvPayrollAmt:int = obj["Rpt1RcvPayrollAmt"]
      """  Received Payroll Amount in reporting Currency  """  
      self.Rpt2RcvPayrollAmt:int = obj["Rpt2RcvPayrollAmt"]
      """  Received Payroll Amount in reporting Currency  """  
      self.Rpt3RcvPayrollAmt:int = obj["Rpt3RcvPayrollAmt"]
      """  Received Payroll Amount in reporting Currency  """  
      self.DocTotalRcvAmt:int = obj["DocTotalRcvAmt"]
      """  Total cash amount received per day with draft document amounts  """  
      self.RcvTotalAmt:int = obj["RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts  """  
      self.Rpt1RcvTotalAmt:int = obj["Rpt1RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts in reporting Currency  """  
      self.Rpt2RcvTotalAmt:int = obj["Rpt2RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts in reporting Currency  """  
      self.Rpt3RcvTotalAmt:int = obj["Rpt3RcvTotalAmt"]
      """  Total cash amount received per day with draft document amounts in reporting Currency.  """  
      self.DocIssCashAmt:int = obj["DocIssCashAmt"]
      """  Total cash amount Issued per day.  """  
      self.IssCashAmt:int = obj["IssCashAmt"]
      """  Total cash amount Issued per day  """  
      self.Rpt1IssCashAmt:int = obj["Rpt1IssCashAmt"]
      """  Total cash amount Issued per day in reporting Currency  """  
      self.Rpt2IssCashAmt:int = obj["Rpt2IssCashAmt"]
      """  Total cash amount Issued per day in reporting Currency  """  
      self.Rpt3IssCashAmt:int = obj["Rpt3IssCashAmt"]
      """  Total cash amount Issued per day in reporting Currency  """  
      self.DocIssPayrollAmt:int = obj["DocIssPayrollAmt"]
      """  Total cash amount Issued per day by payroll operations only  """  
      self.IssPayrollAmt:int = obj["IssPayrollAmt"]
      """  Total cash amount Issued per day by payroll operations only  """  
      self.Rpt1IssPayrollAmt:int = obj["Rpt1IssPayrollAmt"]
      """  Issued Payroll Amount in reporting Currency  """  
      self.Rpt2IssPayrollAmt:int = obj["Rpt2IssPayrollAmt"]
      """  Issued Payroll Amount in reporting Currency  """  
      self.Rpt3IssPayrollAmt:int = obj["Rpt3IssPayrollAmt"]
      """  Issued Payroll Amount in reporting Currency  """  
      self.DocIssTotalAmt:int = obj["DocIssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts  """  
      self.IssTotalAmt:int = obj["IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts  """  
      self.Rpt1IssTotalAmt:int = obj["Rpt1IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts in reporting Currency  """  
      self.Rpt2IssTotalAmt:int = obj["Rpt2IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts in reporting Currency  """  
      self.Rpt3IssTotalAmt:int = obj["Rpt3IssTotalAmt"]
      """  Total cash amount Issued per day with draft document amounts in reporting Currency  """  
      self.DocDayBal:int = obj["DocDayBal"]
      """  Cash Desk Day Closing Balance  """  
      self.DayBal:int = obj["DayBal"]
      """  Cash Desk Day Closing Balance  """  
      self.Rpt1DayBal:int = obj["Rpt1DayBal"]
      """  Cash Desk Day Closing Balance in reporting Currency  """  
      self.Rpt2DayBal:int = obj["Rpt2DayBal"]
      """  Cash Desk Day Closing Balance in reporting Currency  """  
      self.Rpt3DayBal:int = obj["Rpt3DayBal"]
      """  Cash Desk Day Closing Balance in reporting Currency  """  
      self.DocPayrollDayBal:int = obj["DocPayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance  """  
      self.PayrollDayBal:int = obj["PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance  """  
      self.Rpt1PayrollDayBal:int = obj["Rpt1PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance in reporting Currency  """  
      self.Rpt2PayrollDayBal:int = obj["Rpt2PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance in reporting Currency  """  
      self.Rpt3PayrollDayBal:int = obj["Rpt3PayrollDayBal"]
      """  Cash Desk Day Closing Payroll Balance in reporting Currency  """  
      self.DocDayBalWithDraft:int = obj["DocDayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  """  
      self.DayBalWithDraft:int = obj["DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  """  
      self.Rpt1DayBalWithDraft:int = obj["Rpt1DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  """  
      self.Rpt2DayBalWithDraft:int = obj["Rpt2DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  """  
      self.Rpt3DayBalWithDraft:int = obj["Rpt3DayBalWithDraft"]
      """  Cash Desk Day Closing Balance with draft document amounts in reporting Currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GainLossBal:int = obj["GainLossBal"]
      """  GainLossBal  """  
      self.DocGainLossBal:int = obj["DocGainLossBal"]
      """  DocGainLossBal  """  
      self.Rpt1GainLossBal:int = obj["Rpt1GainLossBal"]
      """  Rpt1GainLossBal  """  
      self.Rpt2GainLossBal:int = obj["Rpt2GainLossBal"]
      """  Rpt2GainLossBal  """  
      self.Rpt3GainLossBal:int = obj["Rpt3GainLossBal"]
      """  Rpt3GainLossBal  """  
      self.PrintedOfficial:bool = obj["PrintedOfficial"]
      """  PrintedOfficial  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashCloseDayListTableset:
   def __init__(self, obj):
      self.PCashBalList:list[Erp_Tablesets_PCashBalListRow] = obj["PCashBalList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCashCloseDayTableset:
   def __init__(self, obj):
      self.PCashBal:list[Erp_Tablesets_PCashBalRow] = obj["PCashBal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPCashCloseDayTableset:
   def __init__(self, obj):
      self.PCashBal:list[Erp_Tablesets_PCashBalRow] = obj["PCashBal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   cashDeskID
   date
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      self.date:str = obj["date"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashCloseDayTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashCloseDayTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashCloseDayTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashCloseDayListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPCashBal_input:
   """ Required : 
   ds
   cashDeskID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashCloseDayTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class GetNewPCashBal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashCloseDayTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePCashBal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePCashBal:str = obj["whereClausePCashBal"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashCloseDayTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPCashCloseDayTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCashCloseDayTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashCloseDayTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashCloseDayTableset] = obj["ds"]
      pass

      """  output parameters  """  

