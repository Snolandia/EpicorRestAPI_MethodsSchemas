import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DynAttrValueSvc
# Description: Dyn Attributes value .
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrValues",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company, RelatedToSchemaName, RelatedToTableName, RelatedToSysRowID, AttrClassID, AttributeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrValue item
   Description: Calls GetByID to retrieve the DynAttrValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToTableName: Desc: RelatedToTableName   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company, RelatedToSchemaName, RelatedToTableName, RelatedToSysRowID, AttrClassID, AttributeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrValue for the service
   Description: Calls UpdateExt to update DynAttrValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToTableName: Desc: RelatedToTableName   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company, RelatedToSchemaName, RelatedToTableName, RelatedToSysRowID, AttrClassID, AttributeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrValue item
   Description: Call UpdateExt to delete DynAttrValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToTableName: Desc: RelatedToTableName   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlComboValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtlComboValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlComboValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlComboValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrClassDtlComboValues",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrClassDtlComboValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrClassDtlComboValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlComboValues_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlComboValue item
   Description: Calls GetByID to retrieve the DynAttrClassDtlComboValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlComboValue
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrClassDtlComboValues(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrClassDtlComboValues_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrClassDtlComboValue for the service
   Description: Calls UpdateExt to update DynAttrClassDtlComboValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlComboValue
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrClassDtlComboValues(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrClassDtlComboValues_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrClassDtlComboValue item
   Description: Call UpdateExt to delete DynAttrClassDtlComboValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlComboValue
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/DynAttrClassDtlComboValues(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynAttrValue, whereClauseDynAttrClassDtlComboValues, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseDynAttrValue=" + whereClauseDynAttrValue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrClassDtlComboValues=" + whereClauseDynAttrClassDtlComboValues
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToSchemaName, relatedToTableName, relatedToSysRowID, attrClassID, attributeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "relatedToSchemaName=" + relatedToSchemaName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "relatedToTableName=" + relatedToTableName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "relatedToSysRowID=" + relatedToSysRowID
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateDynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDynAttrValues
   Description: Create DynAttributeValue records
   OperationID: CreateDynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrValue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlComboValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassDtlComboValuesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrValueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrValueRow] = obj["value"]
      pass

class Erp_Tablesets_DynAttrClassDtlComboValuesRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeID:str = obj["AttributeID"]
      self.Code:str = obj["Code"]
      self.Description:str = obj["Description"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.DataCharacter:str = obj["DataCharacter"]
      """  Character Data.  """  
      self.DataDate:str = obj["DataDate"]
      """  Date Data.  """  
      self.DataDecimal:int = obj["DataDecimal"]
      """  Decimal Data.  """  
      self.DataInteger:int = obj["DataInteger"]
      """  Integer Data.  """  
      self.DataLogical:bool = obj["DataLogical"]
      """  Logical Data.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.DataCharacter:str = obj["DataCharacter"]
      """  Character Data.  """  
      self.DataDate:str = obj["DataDate"]
      """  Date Data.  """  
      self.DataDecimal:int = obj["DataDecimal"]
      """  Decimal Data.  """  
      self.DataInteger:int = obj["DataInteger"]
      """  Integer Data.  """  
      self.DataLogical:bool = obj["DataLogical"]
      """  Logical Data.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicates this value is a result of a calculation.  """  
      self.IsActual:bool = obj["IsActual"]
      """  Used for planning to indicates for the set that this was the Actual quantity at that point in time.  """  
      self.FieldValue:str = obj["FieldValue"]
      self.TransportValue:str = obj["TransportValue"]
      self.Active:bool = obj["Active"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.HasBeenVerified:bool = obj["HasBeenVerified"]
      """  System controlled to validate all dynamic attribute values against the set hash key.  If the value has been verified it will not perform the validation again.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this calculated field will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  Controlled by setup on attribute detail in Dynamic Attribute Class Maintenance.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateDynAttrValues_input:
   """ Required : 
   schemaName
   tableName
   attrClassID
   foreignSysRowID
   ds
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Related to Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Table name related to the Dyn atrributes  """  
      self.attrClassID:str = obj["attrClassID"]
      """  Dyn Attribute Class ID  """  
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      """  SysROWID of the related row  """  
      self.ds:list[Erp_Tablesets_DynAttrValueTableset] = obj["ds"]
      pass

class CreateDynAttrValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   attrClassID
   attributeID
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.attrClassID:str = obj["attrClassID"]
      self.attributeID:str = obj["attributeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DynAttrClassDtlComboValuesRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeID:str = obj["AttributeID"]
      self.Code:str = obj["Code"]
      self.Description:str = obj["Description"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.DataCharacter:str = obj["DataCharacter"]
      """  Character Data.  """  
      self.DataDate:str = obj["DataDate"]
      """  Date Data.  """  
      self.DataDecimal:int = obj["DataDecimal"]
      """  Decimal Data.  """  
      self.DataInteger:int = obj["DataInteger"]
      """  Integer Data.  """  
      self.DataLogical:bool = obj["DataLogical"]
      """  Logical Data.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueListTableset:
   def __init__(self, obj):
      self.DynAttrValueList:list[Erp_Tablesets_DynAttrValueListRow] = obj["DynAttrValueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DynAttrValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.DataCharacter:str = obj["DataCharacter"]
      """  Character Data.  """  
      self.DataDate:str = obj["DataDate"]
      """  Date Data.  """  
      self.DataDecimal:int = obj["DataDecimal"]
      """  Decimal Data.  """  
      self.DataInteger:int = obj["DataInteger"]
      """  Integer Data.  """  
      self.DataLogical:bool = obj["DataLogical"]
      """  Logical Data.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicates this value is a result of a calculation.  """  
      self.IsActual:bool = obj["IsActual"]
      """  Used for planning to indicates for the set that this was the Actual quantity at that point in time.  """  
      self.FieldValue:str = obj["FieldValue"]
      self.TransportValue:str = obj["TransportValue"]
      self.Active:bool = obj["Active"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.HasBeenVerified:bool = obj["HasBeenVerified"]
      """  System controlled to validate all dynamic attribute values against the set hash key.  If the value has been verified it will not perform the validation again.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this calculated field will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  Controlled by setup on attribute detail in Dynamic Attribute Class Maintenance.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueTableset:
   def __init__(self, obj):
      self.DynAttrValue:list[Erp_Tablesets_DynAttrValueRow] = obj["DynAttrValue"]
      self.DynAttrClassDtlComboValues:list[Erp_Tablesets_DynAttrClassDtlComboValuesRow] = obj["DynAttrClassDtlComboValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDynAttrValueTableset:
   def __init__(self, obj):
      self.DynAttrValue:list[Erp_Tablesets_DynAttrValueRow] = obj["DynAttrValue"]
      self.DynAttrClassDtlComboValues:list[Erp_Tablesets_DynAttrClassDtlComboValuesRow] = obj["DynAttrClassDtlComboValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   attrClassID
   attributeID
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.attrClassID:str = obj["attrClassID"]
      self.attributeID:str = obj["attributeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrValueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrValueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrValueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrValueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDynAttrValue_input:
   """ Required : 
   ds
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   attrClassID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueTableset] = obj["ds"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.attrClassID:str = obj["attrClassID"]
      pass

class GetNewDynAttrValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynAttrValue
   whereClauseDynAttrClassDtlComboValues
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValue:str = obj["whereClauseDynAttrValue"]
      self.whereClauseDynAttrClassDtlComboValues:str = obj["whereClauseDynAttrClassDtlComboValues"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrValueTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtDynAttrValueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrValueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueTableset] = obj["ds"]
      pass

      """  output parameters  """  

