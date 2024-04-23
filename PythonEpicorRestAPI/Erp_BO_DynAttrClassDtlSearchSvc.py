import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DynAttrClassDtlSearchSvc
# Description: Search class for DynAttrClassDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrClassDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlSearches_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlSearch item
   Description: Calls GetByID to retrieve the DynAttrClassDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches(" + Company + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrClassDtlSearches_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrClassDtlSearch for the service
   Description: Calls UpdateExt to update DynAttrClassDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches(" + Company + "," + AttrClassID + "," + AttributeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrClassDtlSearches_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrClassDtlSearch item
   Description: Call UpdateExt to delete DynAttrClassDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches(" + Company + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynAttrClassDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDynAttrClassDtl=" + whereClauseDynAttrClassDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(attrClassID, attributeID, epicorHeaders = None):
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
   params += "attrClassID=" + attrClassID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attributeID=" + attributeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BuildAttributeDelimitedString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAttributeDelimitedString
   Description: Builds a list of attributes separated by ~.  Each attribute is made up of the following separated by `:
1. SysRowID of DynAttrClassDtl record
2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
3. The attribute value to filter on
   OperationID: BuildAttributeDelimitedString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAttributeDelimitedString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeDelimitedString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildAttributeDelimitedStringDisplayString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAttributeDelimitedStringDisplayString
   Description: 1. Builds a list of selected attributes and values for display.
2. Builds a list of attributes separated by ~.  Each attribute is made up of the following separated by `:
a. SysRowID of DynAttrClassDtl record
b. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
c. The attribute value to filter on
   OperationID: BuildAttributeDelimitedStringDisplayString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAttributeDelimitedStringDisplayString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeDelimitedStringDisplayString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildAttributeWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAttributeWhereClause
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause
   OperationID: BuildAttributeWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAttributeWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildAttributeWhereClauseForLotTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAttributeWhereClauseForLotTracker
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause
   OperationID: BuildAttributeWhereClauseForLotTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAttributeWhereClauseForLotTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeWhereClauseForLotTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMetaFxDynamicWebPanelContent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMetaFxDynamicWebPanelContent
   Description: Returns a string containing MetaFX json for use in a dynamic panel. This will contains a list of controls for each attribute available
in the selected attribute class
   OperationID: GetMetaFxDynamicWebPanelContent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMetaFxDynamicWebPanelContent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMetaFxDynamicWebPanelContent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrClassDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrClassDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClassDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClassDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClassDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassDtlRow] = obj["value"]
      pass

class Erp_Tablesets_DynAttrClassDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this attribute.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used when linked to a numeric input.  """  
      self.InitialCharacter:str = obj["InitialCharacter"]
      """  Initial character value.  """  
      self.InitialDate:str = obj["InitialDate"]
      """  Initial date value.  """  
      self.InitialDecimal:int = obj["InitialDecimal"]
      """  Initial decimal value.  """  
      self.InitialInteger:int = obj["InitialInteger"]
      """  Initial integer value.  """  
      self.InitialLogical:bool = obj["InitialLogical"]
      """  Initial logical value.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.MaxDecimal:int = obj["MaxDecimal"]
      """  The user defined maximum acceptable value when linked to a decimal input.  """  
      self.MaxInteger:int = obj["MaxInteger"]
      """  The user defined maximum acceptable value when linked to an integer input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MinDecimal:int = obj["MinDecimal"]
      """  The user defined minimum acceptable value when linked to a decimal input.  """  
      self.MinInteger:int = obj["MinInteger"]
      """  The user defined minimum acceptable value when linked to an integer input.  """  
      self.WebAttribute:bool = obj["WebAttribute"]
      """  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the business use of the field, valid values are "Quantity,UOM"  """  
      self.UOMAttributeID:str = obj["UOMAttributeID"]
      """  Attribute ID of related UOM linked to quantity.  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  If attribute is used in planning.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicated this attribute will be used as a calculated field.  """  
      self.PlanningBaseUOM:str = obj["PlanningBaseUOM"]
      """  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  """  
      self.PlanningType:str = obj["PlanningType"]
      """  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.IsActual:bool = obj["IsActual"]
      """  The actual transaction value for the attribute set.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  """  
      self.MasterDtlLinked:str = obj["MasterDtlLinked"]
      """  Resuable Attribute linked to this class attribute.  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Attributes are synch to this class attribute.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.IncludeListValueCodeInShortDesc:bool = obj["IncludeListValueCodeInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  """  
      self.IncludeListValueDescriptionInShortDesc:bool = obj["IncludeListValueDescriptionInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this attribute.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used when linked to a numeric input.  """  
      self.InitialCharacter:str = obj["InitialCharacter"]
      """  Initial character value.  """  
      self.InitialDate:str = obj["InitialDate"]
      """  Initial date value.  """  
      self.InitialDecimal:int = obj["InitialDecimal"]
      """  Initial decimal value.  """  
      self.InitialInteger:int = obj["InitialInteger"]
      """  Initial integer value.  """  
      self.InitialLogical:bool = obj["InitialLogical"]
      """  Initial logical value.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.MaxDecimal:int = obj["MaxDecimal"]
      """  The user defined maximum acceptable value when linked to a decimal input.  """  
      self.MaxInteger:int = obj["MaxInteger"]
      """  The user defined maximum acceptable value when linked to an integer input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MinDecimal:int = obj["MinDecimal"]
      """  The user defined minimum acceptable value when linked to a decimal input.  """  
      self.MinInteger:int = obj["MinInteger"]
      """  The user defined minimum acceptable value when linked to an integer input.  """  
      self.WebAttribute:bool = obj["WebAttribute"]
      """  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the business use of the field, valid values are "Quantity,UOM"  """  
      self.UOMAttributeID:str = obj["UOMAttributeID"]
      """  Attribute ID of related UOM linked to quantity.  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  If attribute is used in planning.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicated this attribute will be used as a calculated field.  """  
      self.PlanningBaseUOM:str = obj["PlanningBaseUOM"]
      """  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  """  
      self.PlanningType:str = obj["PlanningType"]
      """  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.IsActual:bool = obj["IsActual"]
      """  The actual transaction value for the attribute set.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  """  
      self.MasterDtlLinked:str = obj["MasterDtlLinked"]
      """  Resuable Attribute linked to this class attribute.  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Attributes are synch to this class attribute.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.IncludeListValueCodeInShortDesc:bool = obj["IncludeListValueCodeInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  """  
      self.IncludeListValueDescriptionInShortDesc:bool = obj["IncludeListValueDescriptionInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  """  
      self.InUse:bool = obj["InUse"]
      """  Used for setting Epi Shape to highlight attribute has been used.  """  
      self.ListValues:str = obj["ListValues"]
      """  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  """  
      self.IsFinalExpression:bool = obj["IsFinalExpression"]
      """  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  """  
      self.FinalExpressionUOM:str = obj["FinalExpressionUOM"]
      """  The UOM used with final expression, used to calculate inventory quantity.  """  
      self.RequiredAtAvailableCodes:str = obj["RequiredAtAvailableCodes"]
      """  List of available Required At codes.  """  
      self.RequiredAtAvailableDesc:str = obj["RequiredAtAvailableDesc"]
      """  List of available Required at descriptions.  """  
      self.RequiredAtSelectedCodes:str = obj["RequiredAtSelectedCodes"]
      """  List of Required At codes selected.  """  
      self.RequiredAtSelectedDesc:str = obj["RequiredAtSelectedDesc"]
      """  List of Required At descriptions selected.  """  
      self.IsExpressionDefined:bool = obj["IsExpressionDefined"]
      """  Indicates if this calculated field has a Formula Expression already been added or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildAttributeDelimitedStringDisplayString_input:
   """ Required : 
   attrClassID
   dt
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.dt      #schema had no properties on an object.
      pass

class BuildAttributeDelimitedStringDisplayString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeDelimitedList:str = obj["parameters"]
      self.attributeDisplayValues:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildAttributeDelimitedString_input:
   """ Required : 
   dt
   """  
   def __init__(self, obj):
      self.dt      #schema had no properties on an object.
      pass

class BuildAttributeDelimitedString_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class BuildAttributeWhereClauseForLotTracker_input:
   """ Required : 
   attrClassID
   attributeListString
   whereClause
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  AttrClassID value  """  
      self.attributeListString:str = obj["attributeListString"]
      """  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  """  
      self.whereClause:str = obj["whereClause"]
      """  The whereClause to append to  """  
      pass

class BuildAttributeWhereClauseForLotTracker_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class BuildAttributeWhereClause_input:
   """ Required : 
   attrClassID
   attributeListString
   whereClause
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  AttrClassID value  """  
      self.attributeListString:str = obj["attributeListString"]
      """  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  """  
      self.whereClause:str = obj["whereClause"]
      """  The whereClause to append to  """  
      pass

class BuildAttributeWhereClause_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   attrClassID
   attributeID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.attributeID:str = obj["attributeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DynAttrClassDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this attribute.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used when linked to a numeric input.  """  
      self.InitialCharacter:str = obj["InitialCharacter"]
      """  Initial character value.  """  
      self.InitialDate:str = obj["InitialDate"]
      """  Initial date value.  """  
      self.InitialDecimal:int = obj["InitialDecimal"]
      """  Initial decimal value.  """  
      self.InitialInteger:int = obj["InitialInteger"]
      """  Initial integer value.  """  
      self.InitialLogical:bool = obj["InitialLogical"]
      """  Initial logical value.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.MaxDecimal:int = obj["MaxDecimal"]
      """  The user defined maximum acceptable value when linked to a decimal input.  """  
      self.MaxInteger:int = obj["MaxInteger"]
      """  The user defined maximum acceptable value when linked to an integer input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MinDecimal:int = obj["MinDecimal"]
      """  The user defined minimum acceptable value when linked to a decimal input.  """  
      self.MinInteger:int = obj["MinInteger"]
      """  The user defined minimum acceptable value when linked to an integer input.  """  
      self.WebAttribute:bool = obj["WebAttribute"]
      """  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the business use of the field, valid values are "Quantity,UOM"  """  
      self.UOMAttributeID:str = obj["UOMAttributeID"]
      """  Attribute ID of related UOM linked to quantity.  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  If attribute is used in planning.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicated this attribute will be used as a calculated field.  """  
      self.PlanningBaseUOM:str = obj["PlanningBaseUOM"]
      """  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  """  
      self.PlanningType:str = obj["PlanningType"]
      """  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.IsActual:bool = obj["IsActual"]
      """  The actual transaction value for the attribute set.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  """  
      self.MasterDtlLinked:str = obj["MasterDtlLinked"]
      """  Resuable Attribute linked to this class attribute.  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Attributes are synch to this class attribute.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.IncludeListValueCodeInShortDesc:bool = obj["IncludeListValueCodeInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  """  
      self.IncludeListValueDescriptionInShortDesc:bool = obj["IncludeListValueDescriptionInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassDtlListTableset:
   def __init__(self, obj):
      self.DynAttrClassDtlList:list[Erp_Tablesets_DynAttrClassDtlListRow] = obj["DynAttrClassDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DynAttrClassDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this attribute.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used when linked to a numeric input.  """  
      self.InitialCharacter:str = obj["InitialCharacter"]
      """  Initial character value.  """  
      self.InitialDate:str = obj["InitialDate"]
      """  Initial date value.  """  
      self.InitialDecimal:int = obj["InitialDecimal"]
      """  Initial decimal value.  """  
      self.InitialInteger:int = obj["InitialInteger"]
      """  Initial integer value.  """  
      self.InitialLogical:bool = obj["InitialLogical"]
      """  Initial logical value.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.MaxDecimal:int = obj["MaxDecimal"]
      """  The user defined maximum acceptable value when linked to a decimal input.  """  
      self.MaxInteger:int = obj["MaxInteger"]
      """  The user defined maximum acceptable value when linked to an integer input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MinDecimal:int = obj["MinDecimal"]
      """  The user defined minimum acceptable value when linked to a decimal input.  """  
      self.MinInteger:int = obj["MinInteger"]
      """  The user defined minimum acceptable value when linked to an integer input.  """  
      self.WebAttribute:bool = obj["WebAttribute"]
      """  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the business use of the field, valid values are "Quantity,UOM"  """  
      self.UOMAttributeID:str = obj["UOMAttributeID"]
      """  Attribute ID of related UOM linked to quantity.  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  If attribute is used in planning.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicated this attribute will be used as a calculated field.  """  
      self.PlanningBaseUOM:str = obj["PlanningBaseUOM"]
      """  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  """  
      self.PlanningType:str = obj["PlanningType"]
      """  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.IsActual:bool = obj["IsActual"]
      """  The actual transaction value for the attribute set.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  """  
      self.MasterDtlLinked:str = obj["MasterDtlLinked"]
      """  Resuable Attribute linked to this class attribute.  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Attributes are synch to this class attribute.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.IncludeListValueCodeInShortDesc:bool = obj["IncludeListValueCodeInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  """  
      self.IncludeListValueDescriptionInShortDesc:bool = obj["IncludeListValueDescriptionInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  """  
      self.InUse:bool = obj["InUse"]
      """  Used for setting Epi Shape to highlight attribute has been used.  """  
      self.ListValues:str = obj["ListValues"]
      """  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  """  
      self.IsFinalExpression:bool = obj["IsFinalExpression"]
      """  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  """  
      self.FinalExpressionUOM:str = obj["FinalExpressionUOM"]
      """  The UOM used with final expression, used to calculate inventory quantity.  """  
      self.RequiredAtAvailableCodes:str = obj["RequiredAtAvailableCodes"]
      """  List of available Required At codes.  """  
      self.RequiredAtAvailableDesc:str = obj["RequiredAtAvailableDesc"]
      """  List of available Required at descriptions.  """  
      self.RequiredAtSelectedCodes:str = obj["RequiredAtSelectedCodes"]
      """  List of Required At codes selected.  """  
      self.RequiredAtSelectedDesc:str = obj["RequiredAtSelectedDesc"]
      """  List of Required At descriptions selected.  """  
      self.IsExpressionDefined:bool = obj["IsExpressionDefined"]
      """  Indicates if this calculated field has a Formula Expression already been added or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassDtlSearchTableset:
   def __init__(self, obj):
      self.DynAttrClassDtl:list[Erp_Tablesets_DynAttrClassDtlRow] = obj["DynAttrClassDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDynAttrClassDtlSearchTableset:
   def __init__(self, obj):
      self.DynAttrClassDtl:list[Erp_Tablesets_DynAttrClassDtlRow] = obj["DynAttrClassDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   attrClassID
   attributeID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.attributeID:str = obj["attributeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrClassDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMetaFxDynamicWebPanelContent_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      pass

class GetMetaFxDynamicWebPanelContent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sContent:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewDynAttrClassDtl_input:
   """ Required : 
   ds
   attrClassID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["ds"]
      self.attrClassID:str = obj["attrClassID"]
      pass

class GetNewDynAttrClassDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynAttrClassDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrClassDtl:str = obj["whereClauseDynAttrClassDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtDynAttrClassDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrClassDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

