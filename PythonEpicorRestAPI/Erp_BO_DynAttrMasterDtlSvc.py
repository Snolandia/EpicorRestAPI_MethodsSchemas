import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DynAttrMasterDtlSvc
# Description: Master Dynamic Attributes Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrMasterDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrMasterDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrMasterDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrMasterDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrMasterDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrMasterDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrMasterDtls_Company_AttributeID(Company, AttributeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrMasterDtl item
   Description: Calls GetByID to retrieve the DynAttrMasterDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrMasterDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls(" + Company + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrMasterDtls_Company_AttributeID(Company, AttributeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrMasterDtl for the service
   Description: Calls UpdateExt to update DynAttrMasterDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrMasterDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls(" + Company + "," + AttributeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrMasterDtls_Company_AttributeID(Company, AttributeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrMasterDtl item
   Description: Call UpdateExt to delete DynAttrMasterDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrMasterDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls(" + Company + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrMasterDtls_Company_AttributeID_DynAttrMasterDtlListVals(Company, AttributeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DynAttrMasterDtlListVals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrMasterDtlListVals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrMasterDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls(" + Company + "," + AttributeID + ")/DynAttrMasterDtlListVals",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrMasterDtls_Company_AttributeID_DynAttrMasterDtlListVals_Company_AttributeID_Code(Company, AttributeID, Code, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrMasterDtlListVal item
   Description: Calls GetByID to retrieve the DynAttrMasterDtlListVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrMasterDtlListVal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtls(" + Company + "," + AttributeID + ")/DynAttrMasterDtlListVals(" + Company + "," + AttributeID + "," + Code + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrMasterDtlListVals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrMasterDtlListVals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrMasterDtlListVals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrMasterDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtlListVals",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrMasterDtlListVals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrMasterDtlListVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlListValRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlListValRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtlListVals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrMasterDtlListVals_Company_AttributeID_Code(Company, AttributeID, Code, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrMasterDtlListVal item
   Description: Calls GetByID to retrieve the DynAttrMasterDtlListVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrMasterDtlListVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtlListVals(" + Company + "," + AttributeID + "," + Code + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrMasterDtlListVals_Company_AttributeID_Code(Company, AttributeID, Code, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrMasterDtlListVal for the service
   Description: Calls UpdateExt to update DynAttrMasterDtlListVal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrMasterDtlListVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrMasterDtlListValRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtlListVals(" + Company + "," + AttributeID + "," + Code + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrMasterDtlListVals_Company_AttributeID_Code(Company, AttributeID, Code, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrMasterDtlListVal item
   Description: Call UpdateExt to delete DynAttrMasterDtlListVal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrMasterDtlListVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/DynAttrMasterDtlListVals(" + Company + "," + AttributeID + "," + Code + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrMasterDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynAttrMasterDtl, whereClauseDynAttrMasterDtlListVal, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDynAttrMasterDtl=" + whereClauseDynAttrMasterDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrMasterDtlListVal=" + whereClauseDynAttrMasterDtlListVal
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(attributeID, epicorHeaders = None):
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
   params += "attributeID=" + attributeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFormat
   Description: Validates data format
   OperationID: ValidateFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFieldDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFieldDataType
   Description: Used when the Data Type field of DynAttrMasterDtl has been changed to a new value.
Resets all possible fields.
   OperationID: OnChangeFieldDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFieldDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFieldDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrMasterDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrMasterDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrMasterDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrMasterDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrMasterDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrMasterDtlListVal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrMasterDtlListVal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrMasterDtlListVal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrMasterDtlListVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrMasterDtlListVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrMasterDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrMasterDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrMasterDtlListValRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrMasterDtlListValRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrMasterDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrMasterDtlRow] = obj["value"]
      pass

class Erp_Tablesets_DynAttrMasterDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of Attribute.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this Attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this Attribute.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this Attribute will be read only in Attribute Entry.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in Attribute Entry.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrMasterDtlListValRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of Attribute.  """  
      self.Code:str = obj["Code"]
      """  Code value that will be store in the DynAttrValue.  """  
      self.Description:str = obj["Description"]
      """  Description of list value that will show in list.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute List Value is Active. Default is false.  Once Active, the system will allow it to be used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrMasterDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of Attribute.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this Attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this Attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this Attribute.  """  
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
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this Attribute will be read only in Attribute Entry.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in Attribute Entry.  """  
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
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InUse:bool = obj["InUse"]
      """  Used for setting EpiShape to highlight attribute has been used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   attributeID
   """  
   def __init__(self, obj):
      self.attributeID:str = obj["attributeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DynAttrMasterDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of Attribute.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this Attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this Attribute.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this Attribute will be read only in Attribute Entry.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in Attribute Entry.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrMasterDtlListTableset:
   def __init__(self, obj):
      self.DynAttrMasterDtlList:list[Erp_Tablesets_DynAttrMasterDtlListRow] = obj["DynAttrMasterDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DynAttrMasterDtlListValRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of Attribute.  """  
      self.Code:str = obj["Code"]
      """  Code value that will be store in the DynAttrValue.  """  
      self.Description:str = obj["Description"]
      """  Description of list value that will show in list.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute List Value is Active. Default is false.  Once Active, the system will allow it to be used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrMasterDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of Attribute.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this Attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this Attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this Attribute.  """  
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
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this Attribute will be read only in Attribute Entry.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in Attribute Entry.  """  
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
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InUse:bool = obj["InUse"]
      """  Used for setting EpiShape to highlight attribute has been used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrMasterDtlTableset:
   def __init__(self, obj):
      self.DynAttrMasterDtl:list[Erp_Tablesets_DynAttrMasterDtlRow] = obj["DynAttrMasterDtl"]
      self.DynAttrMasterDtlListVal:list[Erp_Tablesets_DynAttrMasterDtlListValRow] = obj["DynAttrMasterDtlListVal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDynAttrMasterDtlTableset:
   def __init__(self, obj):
      self.DynAttrMasterDtl:list[Erp_Tablesets_DynAttrMasterDtlRow] = obj["DynAttrMasterDtl"]
      self.DynAttrMasterDtlListVal:list[Erp_Tablesets_DynAttrMasterDtlListValRow] = obj["DynAttrMasterDtlListVal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   attributeID
   """  
   def __init__(self, obj):
      self.attributeID:str = obj["attributeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrMasterDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDynAttrMasterDtlListVal_input:
   """ Required : 
   ds
   attributeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      self.attributeID:str = obj["attributeID"]
      pass

class GetNewDynAttrMasterDtlListVal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDynAttrMasterDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

class GetNewDynAttrMasterDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynAttrMasterDtl
   whereClauseDynAttrMasterDtlListVal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrMasterDtl:str = obj["whereClauseDynAttrMasterDtl"]
      self.whereClauseDynAttrMasterDtlListVal:str = obj["whereClauseDynAttrMasterDtlListVal"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["returnObj"]
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

class OnChangeFieldDataType_input:
   """ Required : 
   newDataType
   ds
   """  
   def __init__(self, obj):
      self.newDataType:str = obj["newDataType"]
      """  The new data type value.  """  
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

class OnChangeFieldDataType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrMasterDtlTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrMasterDtlTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFormat_input:
   """ Required : 
   newFieldFormat
   ds
   """  
   def __init__(self, obj):
      self.newFieldFormat:str = obj["newFieldFormat"]
      """  newFieldFormat  """  
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

class ValidateFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

