import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLCOARefTypeSvc
# Description: Used to maintain chart of account reference types by segment
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLCOARefTypes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCOARefTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCOARefTypes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCOARefTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes",headers=creds) as resp:
           return await resp.json()

async def post_GLCOARefTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCOARefTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLCOARefTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLCOARefTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCOARefTypes_Company_COACode_SegmentNbr_RefType(Company, COACode, SegmentNbr, RefType, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCOARefType item
   Description: Calls GetByID to retrieve the GLCOARefType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCOARefType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCOARefTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCOARefTypes_Company_COACode_SegmentNbr_RefType(Company, COACode, SegmentNbr, RefType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCOARefType for the service
   Description: Calls UpdateExt to update GLCOARefType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCOARefType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLCOARefTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCOARefTypes_Company_COACode_SegmentNbr_RefType(Company, COACode, SegmentNbr, RefType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCOARefType item
   Description: Call UpdateExt to delete GLCOARefType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCOARefType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCOARefTypes_Company_COACode_SegmentNbr_RefType_GLCOARefAccts(Company, COACode, SegmentNbr, RefType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLCOARefAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLCOARefAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCOARefAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + ")/GLCOARefAccts",headers=creds) as resp:
           return await resp.json()

async def get_GLCOARefTypes_Company_COACode_SegmentNbr_RefType_GLCOARefAccts_Company_COACode_SegmentNbr_RefType_GLAccount(Company, COACode, SegmentNbr, RefType, GLAccount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCOARefAcct item
   Description: Calls GetByID to retrieve the GLCOARefAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCOARefAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCOARefAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefTypes(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + ")/GLCOARefAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + "," + GLAccount + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCOARefAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCOARefAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCOARefAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCOARefAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefAccts",headers=creds) as resp:
           return await resp.json()

async def post_GLCOARefAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCOARefAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLCOARefAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLCOARefAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCOARefAccts_Company_COACode_SegmentNbr_RefType_GLAccount(Company, COACode, SegmentNbr, RefType, GLAccount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCOARefAcct item
   Description: Calls GetByID to retrieve the GLCOARefAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCOARefAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCOARefAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + "," + GLAccount + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCOARefAccts_Company_COACode_SegmentNbr_RefType_GLAccount(Company, COACode, SegmentNbr, RefType, GLAccount, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCOARefAcct for the service
   Description: Calls UpdateExt to update GLCOARefAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCOARefAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLCOARefAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + "," + GLAccount + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCOARefAccts_Company_COACode_SegmentNbr_RefType_GLAccount(Company, COACode, SegmentNbr, RefType, GLAccount, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCOARefAcct item
   Description: Call UpdateExt to delete GLCOARefAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCOARefAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param RefType: Desc: RefType   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/GLCOARefAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + RefType + "," + GLAccount + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCOARefTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLCOARefType, whereClauseGLCOARefAcct, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLCOARefType=" + whereClauseGLCOARefType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLCOARefAcct=" + whereClauseGLCOARefAcct
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, segmentNbr, refType, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
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
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "segmentNbr=" + segmentNbr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "refType=" + refType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DefaultCOACodeSegments(epicorHeaders = None):
   """  
   Summary: Invoke method DefaultCOACodeSegments
   Description: Purpose:  Check the MasterCOA, if it exists, to see if it has ref type segments.
If so, default the combo box to this value.  Otherwise, find the first
COACode with a ref type segment and set combo boxes
Parameters:
<param name="opCOACode">COA to set combo box</param><param name="opCOADesc">COA Description to display in the combo box</param><param name="opSegmentNbr">Segment Number to set combo box</param><param name="opSegmentName">Segment Name to display in the combo box</param><param name="opMasterCOA">Indentifies the master coa</param>
Notes:  Called during onFormLoaded
   OperationID: DefaultCOACodeSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultCOACodeSegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DefaultFirstCOARefSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultFirstCOARefSegment
   Description: Purpose:  Retrieve number and name of the first segment having GLCOARefType.
Parameters:
<param name="coaCode">COA</param><param name="segmentNbr">Segment Number to set combo box</param><param name="segmentName">Segment Name to display in the combo box</param>
   OperationID: DefaultFirstCOARefSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultFirstCOARefSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultFirstCOARefSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LookForRefEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LookForRefEntities
   Description: Purpose:  Verify the entered COA has ref entity segments of type GLCOAReftype
Parameters:
<param name="ipCOACode">COA Code - Chart of Accounts</param>
Notes:
   OperationID: LookForRefEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookForRefEntities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookForRefEntities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSegmentNbr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSegmentNbr
   Description: Verify entered segment
   OperationID: ValidateSegmentNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSegmentNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSegmentNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLCOARefType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLCOARefType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLCOARefType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLCOARefType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLCOARefType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLCOARefAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLCOARefAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLCOARefAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLCOARefAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLCOARefAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCOARefTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCOARefAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCOARefAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCOARefTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCOARefTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCOARefTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCOARefTypeRow] = obj["value"]
      pass

class Erp_Tablesets_GLCOARefAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.RefType:str = obj["RefType"]
      """  A string that uniquely identifies the code  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RefStatus:str = obj["RefStatus"]
      """   The valid values for Reference Status are:
E = Excluded (no reference code allowed)
O = Optional
R = Required (reference code is mandatory)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefTypeList:str = obj["RefTypeList"]
      """  List of reference types available for use in the list picker  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCOARefTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.RefType:str = obj["RefType"]
      """  A string that uniquely identifies the code  """  
      self.RefTypeDesc:str = obj["RefTypeDesc"]
      """  Description of the Reference type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  External field used to enable static filters on UI side to function  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Indicates if the COACode is the master COA.  """  
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      """  Name of Segment  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCOARefTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.RefType:str = obj["RefType"]
      """  A string that uniquely identifies the code  """  
      self.RefTypeDesc:str = obj["RefTypeDesc"]
      """  Description of the Reference type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  External field used to enable static filters on UI side to function  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Indicates if the COACode is the master COA.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DefaultCOACodeSegments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCOACode:str = obj["parameters"]
      self.opCOADesc:str = obj["parameters"]
      self.opSegmentNbr:int = obj["parameters"]
      self.opSegmentName:str = obj["parameters"]
      self.opMasterCOA:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultFirstCOARefSegment_input:
   """ Required : 
   coaCode
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      pass

class DefaultFirstCOARefSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.segmentNbr:int = obj["parameters"]
      self.segmentName:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   coACode
   segmentNbr
   refType
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.refType:str = obj["refType"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLCOARefAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.RefType:str = obj["RefType"]
      """  A string that uniquely identifies the code  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RefStatus:str = obj["RefStatus"]
      """   The valid values for Reference Status are:
E = Excluded (no reference code allowed)
O = Optional
R = Required (reference code is mandatory)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefTypeList:str = obj["RefTypeList"]
      """  List of reference types available for use in the list picker  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCOARefTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.RefType:str = obj["RefType"]
      """  A string that uniquely identifies the code  """  
      self.RefTypeDesc:str = obj["RefTypeDesc"]
      """  Description of the Reference type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  External field used to enable static filters on UI side to function  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Indicates if the COACode is the master COA.  """  
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      """  Name of Segment  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCOARefTypeListTableset:
   def __init__(self, obj):
      self.GLCOARefTypeList:list[Erp_Tablesets_GLCOARefTypeListRow] = obj["GLCOARefTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLCOARefTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.RefType:str = obj["RefType"]
      """  A string that uniquely identifies the code  """  
      self.RefTypeDesc:str = obj["RefTypeDesc"]
      """  Description of the Reference type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  External field used to enable static filters on UI side to function  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Indicates if the COACode is the master COA.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCOARefTypeTableset:
   def __init__(self, obj):
      self.GLCOARefType:list[Erp_Tablesets_GLCOARefTypeRow] = obj["GLCOARefType"]
      self.GLCOARefAcct:list[Erp_Tablesets_GLCOARefAcctRow] = obj["GLCOARefAcct"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLCOARefTypeTableset:
   def __init__(self, obj):
      self.GLCOARefType:list[Erp_Tablesets_GLCOARefTypeRow] = obj["GLCOARefType"]
      self.GLCOARefAcct:list[Erp_Tablesets_GLCOARefAcctRow] = obj["GLCOARefAcct"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   coACode
   segmentNbr
   refType
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.refType:str = obj["refType"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLCOARefTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLCOARefAcct_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   refType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.refType:str = obj["refType"]
      pass

class GetNewGLCOARefAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLCOARefType_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class GetNewGLCOARefType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLCOARefType
   whereClauseGLCOARefAcct
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLCOARefType:str = obj["whereClauseGLCOARefType"]
      self.whereClauseGLCOARefAcct:str = obj["whereClauseGLCOARefAcct"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["returnObj"]
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

class LookForRefEntities_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      pass

class LookForRefEntities_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLCOARefTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLCOARefTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCOARefTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSegmentNbr_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment number  """  
      pass

class ValidateSegmentNbr_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Bool  """  
      pass

