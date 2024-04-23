import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CreditTranSvc
# Description: Credit Transaction Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CreditTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans",headers=creds) as resp:
           return await resp.json()

async def post_CreditTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditTrans_Company_TranDate_TranTime_TranNum(Company, TranDate, TranTime, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditTran item
   Description: Calls GetByID to retrieve the CreditTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranTime: Desc: TranTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans(" + Company + "," + TranDate + "," + TranTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditTrans_Company_TranDate_TranTime_TranNum(Company, TranDate, TranTime, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditTran for the service
   Description: Calls UpdateExt to update CreditTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranTime: Desc: TranTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans(" + Company + "," + TranDate + "," + TranTime + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditTrans_Company_TranDate_TranTime_TranNum(Company, TranDate, TranTime, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditTran item
   Description: Call UpdateExt to delete CreditTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranTime: Desc: TranTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/CreditTrans(" + Company + "," + TranDate + "," + TranTime + "," + TranNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCreditTran, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCreditTran=" + whereClauseCreditTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tranDate, tranTime, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "tranDate=" + tranDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranTime=" + tranTime
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForCreditCard(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForCreditCard
   Description: Filter by Credit Card Fields
   OperationID: GetRowsForCreditCard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForCreditCard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCreditCard_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForApplyCreditMemo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForApplyCreditMemo
   Description: Returns a list Dataset containing the Deposit and Sale transactions with remaining balance.
The Transaction balance is calculated by subtracting Credit transactions (TranType = C) to TranAmt.
It is used for ApplyCM.
   OperationID: GetListForApplyCreditMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForApplyCreditMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForApplyCreditMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCardNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCardNumbers
   Description: Returns a list Dataset containing the valid credit card numbers already used
for the current customer and currency code.
It is used in Sales Order and Cash Receipt for Credit Card Number search grid.
   OperationID: GetCardNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCardNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCardNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCreditTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCreditTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditTranRow] = obj["value"]
      pass

class Erp_Tablesets_CreditTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.TranTime:int = obj["TranTime"]
      """  Part of the unique key  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.TranTotal:int = obj["TranTotal"]
      """  Transaction Total in base currency.  """  
      self.DocTranTotal:int = obj["DocTranTotal"]
      """  Transaction Total in document currency.  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.AuthCode:str = obj["AuthCode"]
      """  Autherisation Code  """  
      self.Result:str = obj["Result"]
      """  Error code returned by processing company  """  
      self.ResponseMsg:str = obj["ResponseMsg"]
      """  Response Message  """  
      self.AVSAddr:str = obj["AVSAddr"]
      """  result of the address verification  """  
      self.AVSZip:str = obj["AVSZip"]
      """  Result of the address zip verification  """  
      self.CSCMatch:str = obj["CSCMatch"]
      """  Result of the credit security code check  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.CardType:str = obj["CardType"]
      """  A unique identifier for a specific credit card type assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Transaction Type Description  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.ExpMonth:int = obj["ExpMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpYear:int = obj["ExpYear"]
      """  The expiration year of the credit card.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.StAddress:str = obj["StAddress"]
      """  ST Link Address  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.AuthUsed:bool = obj["AuthUsed"]
      """  Flag to indicate that a prior process has used this authorization  """  
      self.CardStore:str = obj["CardStore"]
      """  Encrypted Credit Card Number  """  
      self.Freight:int = obj["Freight"]
      """  Freight Charges in base currency  """  
      self.DocFreight:int = obj["DocFreight"]
      """  Freight Charges in document currency  """  
      self.Tax:int = obj["Tax"]
      """  Tax amount in base currency.  """  
      self.DocTax:int = obj["DocTax"]
      """  Tax amount in document currency.  """  
      self.Amount:int = obj["Amount"]
      """  Transaction Amount in base currency.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Transaction Amount in document currency.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Rpt1Amount:int = obj["Rpt1Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Amount:int = obj["Rpt2Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Amount:int = obj["Rpt3Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt1Freight:int = obj["Rpt1Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt2Freight:int = obj["Rpt2Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt3Freight:int = obj["Rpt3Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranTotal:int = obj["Rpt1TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranTotal:int = obj["Rpt2TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranTotal:int = obj["Rpt3TranTotal"]
      """  Reporting currency value of this field  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of user who made the credit transaction  """  
      self.StrId:str = obj["StrId"]
      """  STLink Identifier  """  
      self.CVNCode:int = obj["CVNCode"]
      """  Result of CVN checl  """  
      self.CVNMessage:str = obj["CVNMessage"]
      """  SVN verification message  """  
      self.ReferrerCode:str = obj["ReferrerCode"]
      """  Referrer Code  """  
      self.PTOrderNum:str = obj["PTOrderNum"]
      """  Order Number created by PaymentTrust if not supplied by process  """  
      self.AuthEntity:str = obj["AuthEntity"]
      """  Authorisation Entity  """  
      self.TranSuccess:bool = obj["TranSuccess"]
      """  Indicates if transaction was successful or not  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToName:str = obj["ShipToName"]
      self.PrcConNum:int = obj["PrcConNum"]
      """  The primary contact for the related order.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  The shipping contact number for the order.  """  
      self.CustID:str = obj["CustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.TranTime:int = obj["TranTime"]
      """  Part of the unique key  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.TranTotal:int = obj["TranTotal"]
      """  Transaction Total in base currency.  """  
      self.DocTranTotal:int = obj["DocTranTotal"]
      """  Transaction Total in document currency.  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.AuthCode:str = obj["AuthCode"]
      """  Autherisation Code  """  
      self.Result:str = obj["Result"]
      """  Error code returned by processing company  """  
      self.ResponseMsg:str = obj["ResponseMsg"]
      """  Response Message  """  
      self.AVSAddr:str = obj["AVSAddr"]
      """  result of the address verification  """  
      self.AVSZip:str = obj["AVSZip"]
      """  Result of the address zip verification  """  
      self.CSCMatch:str = obj["CSCMatch"]
      """  Result of the credit security code check  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.CardType:str = obj["CardType"]
      """  A unique identifier for a specific credit card type assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Transaction Type Description  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.ExpMonth:int = obj["ExpMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpYear:int = obj["ExpYear"]
      """  The expiration year of the credit card.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.StAddress:str = obj["StAddress"]
      """  ST Link Address  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.AuthUsed:bool = obj["AuthUsed"]
      """  Flag to indicate that a prior process has used this authorization  """  
      self.CardStore:str = obj["CardStore"]
      """  Encrypted Credit Card Number  """  
      self.Freight:int = obj["Freight"]
      """  Freight Charges in base currency  """  
      self.DocFreight:int = obj["DocFreight"]
      """  Freight Charges in document currency  """  
      self.Tax:int = obj["Tax"]
      """  Tax amount in base currency.  """  
      self.DocTax:int = obj["DocTax"]
      """  Tax amount in document currency.  """  
      self.Amount:int = obj["Amount"]
      """  Transaction Amount in base currency.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Transaction Amount in document currency.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Rpt1Amount:int = obj["Rpt1Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Amount:int = obj["Rpt2Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Amount:int = obj["Rpt3Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt1Freight:int = obj["Rpt1Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt2Freight:int = obj["Rpt2Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt3Freight:int = obj["Rpt3Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranTotal:int = obj["Rpt1TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranTotal:int = obj["Rpt2TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranTotal:int = obj["Rpt3TranTotal"]
      """  Reporting currency value of this field  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of user who made the credit transaction  """  
      self.StrId:str = obj["StrId"]
      """  STLink Identifier  """  
      self.CVNCode:int = obj["CVNCode"]
      """  Result of CVN checl  """  
      self.CVNMessage:str = obj["CVNMessage"]
      """  SVN verification message  """  
      self.ReferrerCode:str = obj["ReferrerCode"]
      """  Referrer Code  """  
      self.PTOrderNum:str = obj["PTOrderNum"]
      """  Order Number created by PaymentTrust if not supplied by process  """  
      self.AuthEntity:str = obj["AuthEntity"]
      """  Authorisation Entity  """  
      self.TranSuccess:bool = obj["TranSuccess"]
      """  Indicates if transaction was successful or not  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CCCity:str = obj["CCCity"]
      """  CCCity  """  
      self.CCState:str = obj["CCState"]
      """  CCState  """  
      self.FDMSReferenceData:str = obj["FDMSReferenceData"]
      """  FDMS Reference Data used in Deposit and Void transaction.  """  
      self.Processor:str = obj["Processor"]
      """  Processor  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  ISOCurrCode  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name for customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShpConNum:int = obj["ShpConNum"]
      """  The shipping contact number for the order.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  The primary contact for the related order.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tranDate
   tranTime
   tranNum
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      self.tranTime:int = obj["tranTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CreditTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.TranTime:int = obj["TranTime"]
      """  Part of the unique key  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.TranTotal:int = obj["TranTotal"]
      """  Transaction Total in base currency.  """  
      self.DocTranTotal:int = obj["DocTranTotal"]
      """  Transaction Total in document currency.  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.AuthCode:str = obj["AuthCode"]
      """  Autherisation Code  """  
      self.Result:str = obj["Result"]
      """  Error code returned by processing company  """  
      self.ResponseMsg:str = obj["ResponseMsg"]
      """  Response Message  """  
      self.AVSAddr:str = obj["AVSAddr"]
      """  result of the address verification  """  
      self.AVSZip:str = obj["AVSZip"]
      """  Result of the address zip verification  """  
      self.CSCMatch:str = obj["CSCMatch"]
      """  Result of the credit security code check  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.CardType:str = obj["CardType"]
      """  A unique identifier for a specific credit card type assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Transaction Type Description  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.ExpMonth:int = obj["ExpMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpYear:int = obj["ExpYear"]
      """  The expiration year of the credit card.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.StAddress:str = obj["StAddress"]
      """  ST Link Address  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.AuthUsed:bool = obj["AuthUsed"]
      """  Flag to indicate that a prior process has used this authorization  """  
      self.CardStore:str = obj["CardStore"]
      """  Encrypted Credit Card Number  """  
      self.Freight:int = obj["Freight"]
      """  Freight Charges in base currency  """  
      self.DocFreight:int = obj["DocFreight"]
      """  Freight Charges in document currency  """  
      self.Tax:int = obj["Tax"]
      """  Tax amount in base currency.  """  
      self.DocTax:int = obj["DocTax"]
      """  Tax amount in document currency.  """  
      self.Amount:int = obj["Amount"]
      """  Transaction Amount in base currency.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Transaction Amount in document currency.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Rpt1Amount:int = obj["Rpt1Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Amount:int = obj["Rpt2Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Amount:int = obj["Rpt3Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt1Freight:int = obj["Rpt1Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt2Freight:int = obj["Rpt2Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt3Freight:int = obj["Rpt3Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranTotal:int = obj["Rpt1TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranTotal:int = obj["Rpt2TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranTotal:int = obj["Rpt3TranTotal"]
      """  Reporting currency value of this field  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of user who made the credit transaction  """  
      self.StrId:str = obj["StrId"]
      """  STLink Identifier  """  
      self.CVNCode:int = obj["CVNCode"]
      """  Result of CVN checl  """  
      self.CVNMessage:str = obj["CVNMessage"]
      """  SVN verification message  """  
      self.ReferrerCode:str = obj["ReferrerCode"]
      """  Referrer Code  """  
      self.PTOrderNum:str = obj["PTOrderNum"]
      """  Order Number created by PaymentTrust if not supplied by process  """  
      self.AuthEntity:str = obj["AuthEntity"]
      """  Authorisation Entity  """  
      self.TranSuccess:bool = obj["TranSuccess"]
      """  Indicates if transaction was successful or not  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToName:str = obj["ShipToName"]
      self.PrcConNum:int = obj["PrcConNum"]
      """  The primary contact for the related order.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  The shipping contact number for the order.  """  
      self.CustID:str = obj["CustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditTranListTableset:
   def __init__(self, obj):
      self.CreditTranList:list[Erp_Tablesets_CreditTranListRow] = obj["CreditTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CreditTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.TranTime:int = obj["TranTime"]
      """  Part of the unique key  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.TranTotal:int = obj["TranTotal"]
      """  Transaction Total in base currency.  """  
      self.DocTranTotal:int = obj["DocTranTotal"]
      """  Transaction Total in document currency.  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.AuthCode:str = obj["AuthCode"]
      """  Autherisation Code  """  
      self.Result:str = obj["Result"]
      """  Error code returned by processing company  """  
      self.ResponseMsg:str = obj["ResponseMsg"]
      """  Response Message  """  
      self.AVSAddr:str = obj["AVSAddr"]
      """  result of the address verification  """  
      self.AVSZip:str = obj["AVSZip"]
      """  Result of the address zip verification  """  
      self.CSCMatch:str = obj["CSCMatch"]
      """  Result of the credit security code check  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.CardType:str = obj["CardType"]
      """  A unique identifier for a specific credit card type assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Transaction Type Description  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.ExpMonth:int = obj["ExpMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpYear:int = obj["ExpYear"]
      """  The expiration year of the credit card.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.StAddress:str = obj["StAddress"]
      """  ST Link Address  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.AuthUsed:bool = obj["AuthUsed"]
      """  Flag to indicate that a prior process has used this authorization  """  
      self.CardStore:str = obj["CardStore"]
      """  Encrypted Credit Card Number  """  
      self.Freight:int = obj["Freight"]
      """  Freight Charges in base currency  """  
      self.DocFreight:int = obj["DocFreight"]
      """  Freight Charges in document currency  """  
      self.Tax:int = obj["Tax"]
      """  Tax amount in base currency.  """  
      self.DocTax:int = obj["DocTax"]
      """  Tax amount in document currency.  """  
      self.Amount:int = obj["Amount"]
      """  Transaction Amount in base currency.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Transaction Amount in document currency.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Rpt1Amount:int = obj["Rpt1Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Amount:int = obj["Rpt2Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Amount:int = obj["Rpt3Amount"]
      """  Reporting currency value of this field  """  
      self.Rpt1Freight:int = obj["Rpt1Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt2Freight:int = obj["Rpt2Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt3Freight:int = obj["Rpt3Freight"]
      """  Reporting currency value of this field  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranTotal:int = obj["Rpt1TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranTotal:int = obj["Rpt2TranTotal"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranTotal:int = obj["Rpt3TranTotal"]
      """  Reporting currency value of this field  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of user who made the credit transaction  """  
      self.StrId:str = obj["StrId"]
      """  STLink Identifier  """  
      self.CVNCode:int = obj["CVNCode"]
      """  Result of CVN checl  """  
      self.CVNMessage:str = obj["CVNMessage"]
      """  SVN verification message  """  
      self.ReferrerCode:str = obj["ReferrerCode"]
      """  Referrer Code  """  
      self.PTOrderNum:str = obj["PTOrderNum"]
      """  Order Number created by PaymentTrust if not supplied by process  """  
      self.AuthEntity:str = obj["AuthEntity"]
      """  Authorisation Entity  """  
      self.TranSuccess:bool = obj["TranSuccess"]
      """  Indicates if transaction was successful or not  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CCCity:str = obj["CCCity"]
      """  CCCity  """  
      self.CCState:str = obj["CCState"]
      """  CCState  """  
      self.FDMSReferenceData:str = obj["FDMSReferenceData"]
      """  FDMS Reference Data used in Deposit and Void transaction.  """  
      self.Processor:str = obj["Processor"]
      """  Processor  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  ISOCurrCode  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name for customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShpConNum:int = obj["ShpConNum"]
      """  The shipping contact number for the order.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  The primary contact for the related order.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditTranTableset:
   def __init__(self, obj):
      self.CreditTran:list[Erp_Tablesets_CreditTranRow] = obj["CreditTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCreditTranTableset:
   def __init__(self, obj):
      self.CreditTran:list[Erp_Tablesets_CreditTranRow] = obj["CreditTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   tranDate
   tranTime
   tranNum
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      self.tranTime:int = obj["tranTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditTranTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditTranTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditTranTableset] = obj["returnObj"]
      pass

class GetCardNumbers_input:
   """ Required : 
   custNum
   currencyCode
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  CustNum  """  
      self.currencyCode:str = obj["currencyCode"]
      """  CurrencyCode  """  
      pass

class GetCardNumbers_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditTranListTableset] = obj["returnObj"]
      pass

class GetListForApplyCreditMemo_input:
   """ Required : 
   whereClause
   custNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.custNum:int = obj["custNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListForApplyCreditMemo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditTranListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditTranListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCreditTran_input:
   """ Required : 
   ds
   tranDate
   tranTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditTranTableset] = obj["ds"]
      self.tranDate:str = obj["tranDate"]
      self.tranTime:int = obj["tranTime"]
      pass

class GetNewCreditTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseCreditTran
   whereClauseOrderHed
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCreditTran:str = obj["whereClauseCreditTran"]
      """  Where clause for HDCase table.  """  
      self.whereClauseOrderHed:str = obj["whereClauseOrderHed"]
      """  Where clause for OrderHed table.  """  
      self.contactName:str = obj["contactName"]
      """  The contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditTranTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForCreditCard_input:
   """ Required : 
   WhereClause
   inGroupID
   inHeadNum
   inOrderNum
   inCardProcess
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  The where clause.  """  
      self.inGroupID:str = obj["inGroupID"]
      """  CashHead.GroupID field if available  """  
      self.inHeadNum:int = obj["inHeadNum"]
      """  CashHead.HeadNum field if available  """  
      self.inOrderNum:int = obj["inOrderNum"]
      """  CashHead.OrderNum field if available  """  
      self.inCardProcess:str = obj["inCardProcess"]
      """  Encrypted Credit Card.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsForCreditCard_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditTranTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCreditTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCreditTran:str = obj["whereClauseCreditTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditTranTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCreditTranTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCreditTranTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditTranTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

