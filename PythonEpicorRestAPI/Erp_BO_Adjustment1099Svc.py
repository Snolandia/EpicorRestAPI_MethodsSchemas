import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.Adjustment1099Svc
# Description: Adjustment1099 Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Adjustment1099s(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Adjustment1099s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Adjustment1099s
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Adjustment1099Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/Adjustment1099s",headers=creds) as resp:
           return await resp.json()

async def post_Adjustment1099s(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Adjustment1099s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.Adjustment1099Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.Adjustment1099Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/Adjustment1099s", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Adjustment1099s_Company_FormTypeID_AdjustmentNum(Company, FormTypeID, AdjustmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Adjustment1099 item
   Description: Calls GetByID to retrieve the Adjustment1099 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Adjustment1099
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param AdjustmentNum: Desc: AdjustmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.Adjustment1099Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/Adjustment1099s(" + Company + "," + FormTypeID + "," + AdjustmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Adjustment1099s_Company_FormTypeID_AdjustmentNum(Company, FormTypeID, AdjustmentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Adjustment1099 for the service
   Description: Calls UpdateExt to update Adjustment1099. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Adjustment1099
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param AdjustmentNum: Desc: AdjustmentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.Adjustment1099Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/Adjustment1099s(" + Company + "," + FormTypeID + "," + AdjustmentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Adjustment1099s_Company_FormTypeID_AdjustmentNum(Company, FormTypeID, AdjustmentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Adjustment1099 item
   Description: Call UpdateExt to delete Adjustment1099 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Adjustment1099
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FormTypeID: Desc: FormTypeID   Required: True   Allow empty value : True
      :param AdjustmentNum: Desc: AdjustmentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/Adjustment1099s(" + Company + "," + FormTypeID + "," + AdjustmentNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.Adjustment1099ListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAdjustment1099, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAdjustment1099=" + whereClauseAdjustment1099
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(formTypeID, adjustmentNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "formTypeID=" + formTypeID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "adjustmentNum=" + adjustmentNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendor
   Description: Call this method when the user enters the ttAdjustment1099.VendorID
   OperationID: OnChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Change1099Code(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Change1099Code
   Description: Call this method when code 1099 changes
   OperationID: Change1099Code
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Change1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Change1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CleanDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CleanDate
   Description: Call this method to clean the Gen1099 date
   OperationID: CleanDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CleanDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CleanDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFormType(epicorHeaders = None):
   """  
   Summary: Invoke method GetFormType
   Description: Returns the default Form Type when the form is opened the first time
   OperationID: GetFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultFormType(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultFormType
   Description: Obtain Default value for 1099 Form Type combo
   OperationID: GetDefaultFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetByIDSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDSite
   OperationID: GetByIDSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAdjustment1099(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAdjustment1099
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAdjustment1099
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAdjustment1099_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAdjustment1099_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.Adjustment1099Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Adjustment1099ListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_Adjustment1099ListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_Adjustment1099Row:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_Adjustment1099Row] = obj["value"]
      pass

class Erp_Tablesets_Adjustment1099ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.AdjustmentNum:int = obj["AdjustmentNum"]
      """  1099 Adjustment Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Adjustment1099Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.AdjustmentNum:int = obj["AdjustmentNum"]
      """  1099 Adjustment Number  """  
      self.TaxYear:int = obj["TaxYear"]
      """  TaxYear  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.AdjustmentAmt:int = obj["AdjustmentAmt"]
      """  Adjustment Amount  """  
      self.SubmittedAmt:int = obj["SubmittedAmt"]
      """  Submitted Amt  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Generated 1099 Code where this invoice was calculated  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date, stamped with date when adjustment was processed by generation process.  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.FullAddress:str = obj["FullAddress"]
      """  Vendor's full address  """  
      self.FullAddressFormatted:str = obj["FullAddressFormatted"]
      """  Vendor's full address formatted  """  
      self.BitFlag:int = obj["BitFlag"]
      self.Code1099DescDescription:str = obj["Code1099DescDescription"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCode1099ID:str = obj["VendorCode1099ID"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorReporting1099Name2:str = obj["VendorReporting1099Name2"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorName:str = obj["VendorName"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Change1099Code_input:
   """ Required : 
   code1099
   ds
   """  
   def __init__(self, obj):
      self.code1099:str = obj["code1099"]
      """  Code 1099 ID  """  
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

class Change1099Code_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class CleanDate_input:
   """ Required : 
   formType
   adjNum
   ds
   """  
   def __init__(self, obj):
      self.formType:str = obj["formType"]
      """  Form Type  """  
      self.adjNum:int = obj["adjNum"]
      """  Adjustment number  """  
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

class CleanDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   formTypeID
   adjustmentNum
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      self.adjustmentNum:int = obj["adjustmentNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_Adjustment1099ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.AdjustmentNum:int = obj["AdjustmentNum"]
      """  1099 Adjustment Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Adjustment1099ListTableset:
   def __init__(self, obj):
      self.Adjustment1099List:list[Erp_Tablesets_Adjustment1099ListRow] = obj["Adjustment1099List"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_Adjustment1099Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.AdjustmentNum:int = obj["AdjustmentNum"]
      """  1099 Adjustment Number  """  
      self.TaxYear:int = obj["TaxYear"]
      """  TaxYear  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.AdjustmentAmt:int = obj["AdjustmentAmt"]
      """  Adjustment Amount  """  
      self.SubmittedAmt:int = obj["SubmittedAmt"]
      """  Submitted Amt  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Generated 1099 Code where this invoice was calculated  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date, stamped with date when adjustment was processed by generation process.  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.FullAddress:str = obj["FullAddress"]
      """  Vendor's full address  """  
      self.FullAddressFormatted:str = obj["FullAddressFormatted"]
      """  Vendor's full address formatted  """  
      self.BitFlag:int = obj["BitFlag"]
      self.Code1099DescDescription:str = obj["Code1099DescDescription"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCode1099ID:str = obj["VendorCode1099ID"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorReporting1099Name2:str = obj["VendorReporting1099Name2"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorName:str = obj["VendorName"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_Adjustment1099Tableset:
   def __init__(self, obj):
      self.Adjustment1099:list[Erp_Tablesets_Adjustment1099Row] = obj["Adjustment1099"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAdjustment1099Tableset:
   def __init__(self, obj):
      self.Adjustment1099:list[Erp_Tablesets_Adjustment1099Row] = obj["Adjustment1099"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDSite_input:
   """ Required : 
   formTypeID
   adjustmentNum
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      """  1099 Form Type  """  
      self.adjustmentNum:int = obj["adjustmentNum"]
      """  1099 Adjustment Number  """  
      pass

class GetByIDSite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Adjustment1099Tableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   formTypeID
   adjustmentNum
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      self.adjustmentNum:int = obj["adjustmentNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Adjustment1099Tableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_Adjustment1099Tableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_Adjustment1099Tableset] = obj["returnObj"]
      pass

class GetDefaultFormType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultFormType:str = obj["parameters"]
      self.defaultFormTypeDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFormType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.formTypeID:str = obj["parameters"]
      self.description:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_Adjustment1099ListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAdjustment1099_input:
   """ Required : 
   ds
   formTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      self.formTypeID:str = obj["formTypeID"]
      pass

class GetNewAdjustment1099_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAdjustment1099
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAdjustment1099:str = obj["whereClauseAdjustment1099"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_Adjustment1099Tableset] = obj["returnObj"]
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

class OnChangeVendor_input:
   """ Required : 
   vendorNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:str = obj["vendorNum"]
      """  Vendor Num  """  
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

class OnChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAdjustment1099Tableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAdjustment1099Tableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_Adjustment1099Tableset] = obj["ds"]
      pass

      """  output parameters  """  

