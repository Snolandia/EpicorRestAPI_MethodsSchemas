import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlLabelValueSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlLabelValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlLabelValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlLabelValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/PkgControlLabelValues",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlLabelValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlLabelValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/PkgControlLabelValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlLabelValues_Company_Plant_ShipToCustNum_ShipToNum_PartNum(Company, Plant, ShipToCustNum, ShipToNum, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlLabelValue item
   Description: Calls GetByID to retrieve the PkgControlLabelValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustNum: Desc: ShipToCustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/PkgControlLabelValues(" + Company + "," + Plant + "," + ShipToCustNum + "," + ShipToNum + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlLabelValues_Company_Plant_ShipToCustNum_ShipToNum_PartNum(Company, Plant, ShipToCustNum, ShipToNum, PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlLabelValue for the service
   Description: Calls UpdateExt to update PkgControlLabelValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlLabelValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustNum: Desc: ShipToCustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/PkgControlLabelValues(" + Company + "," + Plant + "," + ShipToCustNum + "," + ShipToNum + "," + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlLabelValues_Company_Plant_ShipToCustNum_ShipToNum_PartNum(Company, Plant, ShipToCustNum, ShipToNum, PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlLabelValue item
   Description: Call UpdateExt to delete PkgControlLabelValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlLabelValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustNum: Desc: ShipToCustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/PkgControlLabelValues(" + Company + "," + Plant + "," + ShipToCustNum + "," + ShipToNum + "," + PartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelValueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePkgControlLabelValue, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePkgControlLabelValue=" + whereClausePkgControlLabelValue
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, shipToCustNum, shipToNum, partNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToCustNum=" + shipToCustNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCustomer
   OperationID: ValidateCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShipTo
   OperationID: ValidateShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartNum
   OperationID: ValidatePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedCustID
   OperationID: ChangedCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedShipToNum
   OperationID: ChangedShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedPartNum
   OperationID: ChangedPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlLabelValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlLabelValue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlLabelValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlLabelValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlLabelValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlLabelValueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlLabelValueRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlLabelValueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Identifies the Customer that is associated with this Package Control Label values.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Identifies the Ship To that is associated with this Package Control Label values.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part that is associated with this Package Control Label values.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.Name:str = obj["Name"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Identifies the Customer that is associated with this Package Control Label values.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Identifies the Ship To that is associated with this Package Control Label values.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part that is associated with this Package Control Label values.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangedCustID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

class ChangedCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

class ChangedPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedShipToNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

class ChangedShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   plant
   shipToCustNum
   shipToNum
   partNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.shipToCustNum:int = obj["shipToCustNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.partNum:str = obj["partNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PkgControlLabelValueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Identifies the Customer that is associated with this Package Control Label values.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Identifies the Ship To that is associated with this Package Control Label values.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part that is associated with this Package Control Label values.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.Name:str = obj["Name"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelValueListTableset:
   def __init__(self, obj):
      self.PkgControlLabelValueList:list[Erp_Tablesets_PkgControlLabelValueListRow] = obj["PkgControlLabelValueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlLabelValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Identifies the Customer that is associated with this Package Control Label values.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Identifies the Ship To that is associated with this Package Control Label values.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part that is associated with this Package Control Label values.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelValueTableset:
   def __init__(self, obj):
      self.PkgControlLabelValue:list[Erp_Tablesets_PkgControlLabelValueRow] = obj["PkgControlLabelValue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPkgControlLabelValueTableset:
   def __init__(self, obj):
      self.PkgControlLabelValue:list[Erp_Tablesets_PkgControlLabelValueRow] = obj["PkgControlLabelValue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   shipToCustNum
   shipToNum
   partNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.shipToCustNum:int = obj["shipToCustNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.partNum:str = obj["partNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlLabelValueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPkgControlLabelValue_input:
   """ Required : 
   ds
   plant
   shipToCustNum
   shipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.shipToCustNum:int = obj["shipToCustNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetNewPkgControlLabelValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePkgControlLabelValue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePkgControlLabelValue:str = obj["whereClausePkgControlLabelValue"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPkgControlLabelValueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlLabelValueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCustomer_input:
   """ Required : 
   proposedCustID
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      pass

class ValidateCustomer_output:
   def __init__(self, obj):
      pass

class ValidatePartNum_input:
   """ Required : 
   proposedPartNum
   """  
   def __init__(self, obj):
      self.proposedPartNum:str = obj["proposedPartNum"]
      pass

class ValidatePartNum_output:
   def __init__(self, obj):
      pass

class ValidateShipTo_input:
   """ Required : 
   custNum
   proposedShipTo
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.proposedShipTo:str = obj["proposedShipTo"]
      pass

class ValidateShipTo_output:
   def __init__(self, obj):
      pass

