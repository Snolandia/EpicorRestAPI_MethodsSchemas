import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLCntrlTypeSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCntrlTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCntrlTypes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCntrlTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes",headers=creds) as resp:
           return await resp.json()

async def post_GLCntrlTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCntrlTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLCntrlTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLCntrlTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType(Company, GLControlType, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCntrlType item
   Description: Calls GetByID to retrieve the GLCntrlType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCntrlType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCntrlTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCntrlTypes_Company_GLControlType(Company, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCntrlType for the service
   Description: Calls UpdateExt to update GLCntrlType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCntrlType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLCntrlTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCntrlTypes_Company_GLControlType(Company, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCntrlType item
   Description: Call UpdateExt to delete GLCntrlType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCntrlType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType_GLCTAcctCntxts(Company, GLControlType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLCTAcctCntxts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLCTAcctCntxts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCTAcctCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")/GLCTAcctCntxts",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType_GLCTAcctCntxts_Company_GLControlType_GLCTAcctNum(Company, GLControlType, GLCTAcctNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCTAcctCntxt item
   Description: Calls GetByID to retrieve the GLCTAcctCntxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCTAcctCntxt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param GLCTAcctNum: Desc: GLCTAcctNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCTAcctCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")/GLCTAcctCntxts(" + Company + "," + GLControlType + "," + GLCTAcctNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType_GLCTEntities(Company, GLControlType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLCTEntities items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLCTEntities1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCTEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")/GLCTEntities",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType_GLCTEntities_Company_GLControlType_BusinessEntity(Company, GLControlType, BusinessEntity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCTEntity item
   Description: Calls GetByID to retrieve the GLCTEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCTEntity1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param BusinessEntity: Desc: BusinessEntity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCTEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")/GLCTEntities(" + Company + "," + GLControlType + "," + BusinessEntity + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType_GLCTJrnlCntxts(Company, GLControlType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLCTJrnlCntxts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLCTJrnlCntxts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCTJrnlCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")/GLCTJrnlCntxts",headers=creds) as resp:
           return await resp.json()

async def get_GLCntrlTypes_Company_GLControlType_GLCTJrnlCntxts_Company_GLControlType_JrnlContext(Company, GLControlType, JrnlContext, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCTJrnlCntxt item
   Description: Calls GetByID to retrieve the GLCTJrnlCntxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCTJrnlCntxt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param JrnlContext: Desc: JrnlContext   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCTJrnlCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCntrlTypes(" + Company + "," + GLControlType + ")/GLCTJrnlCntxts(" + Company + "," + GLControlType + "," + JrnlContext + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCTAcctCntxts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCTAcctCntxts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCTAcctCntxts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCTAcctCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTAcctCntxts",headers=creds) as resp:
           return await resp.json()

async def post_GLCTAcctCntxts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCTAcctCntxts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLCTAcctCntxtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLCTAcctCntxtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTAcctCntxts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCTAcctCntxts_Company_GLControlType_GLCTAcctNum(Company, GLControlType, GLCTAcctNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCTAcctCntxt item
   Description: Calls GetByID to retrieve the GLCTAcctCntxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCTAcctCntxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param GLCTAcctNum: Desc: GLCTAcctNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCTAcctCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTAcctCntxts(" + Company + "," + GLControlType + "," + GLCTAcctNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCTAcctCntxts_Company_GLControlType_GLCTAcctNum(Company, GLControlType, GLCTAcctNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCTAcctCntxt for the service
   Description: Calls UpdateExt to update GLCTAcctCntxt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCTAcctCntxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param GLCTAcctNum: Desc: GLCTAcctNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLCTAcctCntxtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTAcctCntxts(" + Company + "," + GLControlType + "," + GLCTAcctNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCTAcctCntxts_Company_GLControlType_GLCTAcctNum(Company, GLControlType, GLCTAcctNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCTAcctCntxt item
   Description: Call UpdateExt to delete GLCTAcctCntxt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCTAcctCntxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param GLCTAcctNum: Desc: GLCTAcctNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTAcctCntxts(" + Company + "," + GLControlType + "," + GLCTAcctNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCTEntities(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCTEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCTEntities
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCTEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTEntities",headers=creds) as resp:
           return await resp.json()

async def post_GLCTEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCTEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLCTEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLCTEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTEntities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCTEntities_Company_GLControlType_BusinessEntity(Company, GLControlType, BusinessEntity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCTEntity item
   Description: Calls GetByID to retrieve the GLCTEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCTEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param BusinessEntity: Desc: BusinessEntity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCTEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTEntities(" + Company + "," + GLControlType + "," + BusinessEntity + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCTEntities_Company_GLControlType_BusinessEntity(Company, GLControlType, BusinessEntity, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCTEntity for the service
   Description: Calls UpdateExt to update GLCTEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCTEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param BusinessEntity: Desc: BusinessEntity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLCTEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTEntities(" + Company + "," + GLControlType + "," + BusinessEntity + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCTEntities_Company_GLControlType_BusinessEntity(Company, GLControlType, BusinessEntity, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCTEntity item
   Description: Call UpdateExt to delete GLCTEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCTEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param BusinessEntity: Desc: BusinessEntity   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTEntities(" + Company + "," + GLControlType + "," + BusinessEntity + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLCTJrnlCntxts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCTJrnlCntxts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCTJrnlCntxts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCTJrnlCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTJrnlCntxts",headers=creds) as resp:
           return await resp.json()

async def post_GLCTJrnlCntxts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCTJrnlCntxts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLCTJrnlCntxtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLCTJrnlCntxtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTJrnlCntxts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCTJrnlCntxts_Company_GLControlType_JrnlContext(Company, GLControlType, JrnlContext, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCTJrnlCntxt item
   Description: Calls GetByID to retrieve the GLCTJrnlCntxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCTJrnlCntxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param JrnlContext: Desc: JrnlContext   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLCTJrnlCntxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTJrnlCntxts(" + Company + "," + GLControlType + "," + JrnlContext + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCTJrnlCntxts_Company_GLControlType_JrnlContext(Company, GLControlType, JrnlContext, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCTJrnlCntxt for the service
   Description: Calls UpdateExt to update GLCTJrnlCntxt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCTJrnlCntxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param JrnlContext: Desc: JrnlContext   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLCTJrnlCntxtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTJrnlCntxts(" + Company + "," + GLControlType + "," + JrnlContext + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCTJrnlCntxts_Company_GLControlType_JrnlContext(Company, GLControlType, JrnlContext, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCTJrnlCntxt item
   Description: Call UpdateExt to delete GLCTJrnlCntxt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCTJrnlCntxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param JrnlContext: Desc: JrnlContext   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/GLCTJrnlCntxts(" + Company + "," + GLControlType + "," + JrnlContext + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLCntrlTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLCntrlType, whereClauseGLCTAcctCntxt, whereClauseGLCTEntity, whereClauseGLCTJrnlCntxt, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseGLCntrlType=" + whereClauseGLCntrlType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLCTAcctCntxt=" + whereClauseGLCTAcctCntxt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLCTEntity=" + whereClauseGLCTEntity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLCTJrnlCntxt=" + whereClauseGLCTJrnlCntxt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glControlType, epicorHeaders = None):
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
   params += "glControlType=" + glControlType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAllBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAllBooks
   Description: Method to call when changing the AllBooks.
   OperationID: ChangeAllBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRequired(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRequired
   Description: Method to call when changing the Required.
   OperationID: ChangeRequired
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRequired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRequired_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUseMasterChart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUseMasterChart
   Description: Method to call when changing the UseMasterChart.
   OperationID: ChangeUseMasterChart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUseMasterChart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseMasterChart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBusinessEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBusinessEntity
   Description: Check list of BusinessEntities for duplicates.
   OperationID: CheckBusinessEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBusinessEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBusinessEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLCntrlType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLCntrlType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLCntrlType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLCntrlType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLCntrlType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLCTAcctCntxt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLCTAcctCntxt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLCTAcctCntxt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLCTAcctCntxt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLCTAcctCntxt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLCTEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLCTEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLCTEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLCTEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLCTEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLCTJrnlCntxt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLCTJrnlCntxt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLCTJrnlCntxt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLCTJrnlCntxt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLCTJrnlCntxt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCntrlTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCTAcctCntxtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCTAcctCntxtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCTEntityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCTEntityRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCTJrnlCntxtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCTJrnlCntxtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCntrlTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCntrlTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLCntrlTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLCntrlTypeRow] = obj["value"]
      pass

class Erp_Tablesets_GLCTAcctCntxtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLCTAcctNum:int = obj["GLCTAcctNum"]
      """  Internal identifier used to keep records unique within a GL Control Type.  The system generates the number on save of a new record by finding the last GLCTAcctCntxt record of a type and adding one to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  Can be blank.  """  
      self.Required:bool = obj["Required"]
      """  Indicates if an account is required on GL Controls that contain this context.  """  
      self.AllBooks:bool = obj["AllBooks"]
      """  Indicates that this context applies to a books.  If this value is true, Book ID is not required.  When a GLControl is created, one GLControlAcct record will be created for this context for each book for the company.  If the value is false and UseMasterChart is false, BookID will be required.  One GLControlAcct record will be created for the context/Book ID combination represented in this record.  """  
      self.UseMasterChart:bool = obj["UseMasterChart"]
      """  Indicate the Master Chart of Accounts is going to be used for this context on GL Controls.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COAName:str = obj["COAName"]
      """  The name of the Master Chart of Accounts.  """  
      self.EnableBookID:bool = obj["EnableBookID"]
      """  Indicates if BookID is available for input.  """  
      self.EnableUseMasterChart:bool = obj["EnableUseMasterChart"]
      """  Indicates if UseMasterChart is available for input.  """  
      self.EnableAllBooks:bool = obj["EnableAllBooks"]
      """  Indicates if AllBooks is available for input  """  
      self.EnableGLAcctContext:bool = obj["EnableGLAcctContext"]
      """  Indicates if the GLAcctContext field is available for input  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCTEntityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  """  
      self.GLCRequirement:str = obj["GLCRequirement"]
      """  Tells if a GlControl required or not, possible options are Stop, Warn, Optional, Inactive  """  
      self.Needed:bool = obj["Needed"]
      """  Indicates if the GL Control is needed by the Business Entity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BusEntitiesDescription:str = obj["BusEntitiesDescription"]
      self.BusEntitiesEntityType:str = obj["BusEntitiesEntityType"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCTJrnlCntxtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.JrnlContext:str = obj["JrnlContext"]
      """  String identifier of a journal context.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The default Journal Code of the Journal that will be used for this context.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCntrlTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Unique Identifier of the GL Control Type assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  GL Control Type description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCntrlTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Unique Identifier of the GL Control Type assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  GL Control Type description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAllBooks_input:
   """ Required : 
   proposedAllBooks
   ds
   """  
   def __init__(self, obj):
      self.proposedAllBooks:bool = obj["proposedAllBooks"]
      """  AllBooks  """  
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

class ChangeAllBooks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRequired_input:
   """ Required : 
   proposedRequired
   vGLControlType
   vGLCTAcctNum
   """  
   def __init__(self, obj):
      self.proposedRequired:bool = obj["proposedRequired"]
      """  Reguired  """  
      self.vGLControlType:str = obj["vGLControlType"]
      """  GLControlType  """  
      self.vGLCTAcctNum:int = obj["vGLCTAcctNum"]
      """  GLCTAcctNum  """  
      pass

class ChangeRequired_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.wmessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeUseMasterChart_input:
   """ Required : 
   proposedUseMasterChart
   ds
   """  
   def __init__(self, obj):
      self.proposedUseMasterChart:bool = obj["proposedUseMasterChart"]
      """  UseMasterChart  """  
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

class ChangeUseMasterChart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBusinessEntity_input:
   """ Required : 
   ProposedBusinessEntity
   ds
   """  
   def __init__(self, obj):
      self.ProposedBusinessEntity:str = obj["ProposedBusinessEntity"]
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

class CheckBusinessEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   glControlType
   """  
   def __init__(self, obj):
      self.glControlType:str = obj["glControlType"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLCTAcctCntxtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLCTAcctNum:int = obj["GLCTAcctNum"]
      """  Internal identifier used to keep records unique within a GL Control Type.  The system generates the number on save of a new record by finding the last GLCTAcctCntxt record of a type and adding one to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  Can be blank.  """  
      self.Required:bool = obj["Required"]
      """  Indicates if an account is required on GL Controls that contain this context.  """  
      self.AllBooks:bool = obj["AllBooks"]
      """  Indicates that this context applies to a books.  If this value is true, Book ID is not required.  When a GLControl is created, one GLControlAcct record will be created for this context for each book for the company.  If the value is false and UseMasterChart is false, BookID will be required.  One GLControlAcct record will be created for the context/Book ID combination represented in this record.  """  
      self.UseMasterChart:bool = obj["UseMasterChart"]
      """  Indicate the Master Chart of Accounts is going to be used for this context on GL Controls.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COAName:str = obj["COAName"]
      """  The name of the Master Chart of Accounts.  """  
      self.EnableBookID:bool = obj["EnableBookID"]
      """  Indicates if BookID is available for input.  """  
      self.EnableUseMasterChart:bool = obj["EnableUseMasterChart"]
      """  Indicates if UseMasterChart is available for input.  """  
      self.EnableAllBooks:bool = obj["EnableAllBooks"]
      """  Indicates if AllBooks is available for input  """  
      self.EnableGLAcctContext:bool = obj["EnableGLAcctContext"]
      """  Indicates if the GLAcctContext field is available for input  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCTEntityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  """  
      self.GLCRequirement:str = obj["GLCRequirement"]
      """  Tells if a GlControl required or not, possible options are Stop, Warn, Optional, Inactive  """  
      self.Needed:bool = obj["Needed"]
      """  Indicates if the GL Control is needed by the Business Entity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BusEntitiesDescription:str = obj["BusEntitiesDescription"]
      self.BusEntitiesEntityType:str = obj["BusEntitiesEntityType"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCTJrnlCntxtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.JrnlContext:str = obj["JrnlContext"]
      """  String identifier of a journal context.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The default Journal Code of the Journal that will be used for this context.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCntrlTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Unique Identifier of the GL Control Type assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  GL Control Type description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCntrlTypeListTableset:
   def __init__(self, obj):
      self.GLCntrlTypeList:list[Erp_Tablesets_GLCntrlTypeListRow] = obj["GLCntrlTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLCntrlTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Unique Identifier of the GL Control Type assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  GL Control Type description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLCntrlTypeTableset:
   def __init__(self, obj):
      self.GLCntrlType:list[Erp_Tablesets_GLCntrlTypeRow] = obj["GLCntrlType"]
      self.GLCTAcctCntxt:list[Erp_Tablesets_GLCTAcctCntxtRow] = obj["GLCTAcctCntxt"]
      self.GLCTEntity:list[Erp_Tablesets_GLCTEntityRow] = obj["GLCTEntity"]
      self.GLCTJrnlCntxt:list[Erp_Tablesets_GLCTJrnlCntxtRow] = obj["GLCTJrnlCntxt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLCntrlTypeTableset:
   def __init__(self, obj):
      self.GLCntrlType:list[Erp_Tablesets_GLCntrlTypeRow] = obj["GLCntrlType"]
      self.GLCTAcctCntxt:list[Erp_Tablesets_GLCTAcctCntxtRow] = obj["GLCTAcctCntxt"]
      self.GLCTEntity:list[Erp_Tablesets_GLCTEntityRow] = obj["GLCTEntity"]
      self.GLCTJrnlCntxt:list[Erp_Tablesets_GLCTJrnlCntxtRow] = obj["GLCTJrnlCntxt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glControlType
   """  
   def __init__(self, obj):
      self.glControlType:str = obj["glControlType"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLCntrlTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLCTAcctCntxt_input:
   """ Required : 
   ds
   glControlType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      self.glControlType:str = obj["glControlType"]
      pass

class GetNewGLCTAcctCntxt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLCTEntity_input:
   """ Required : 
   ds
   glControlType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      self.glControlType:str = obj["glControlType"]
      pass

class GetNewGLCTEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLCTJrnlCntxt_input:
   """ Required : 
   ds
   glControlType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      self.glControlType:str = obj["glControlType"]
      pass

class GetNewGLCTJrnlCntxt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLCntrlType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

class GetNewGLCntrlType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLCntrlType
   whereClauseGLCTAcctCntxt
   whereClauseGLCTEntity
   whereClauseGLCTJrnlCntxt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLCntrlType:str = obj["whereClauseGLCntrlType"]
      self.whereClauseGLCTAcctCntxt:str = obj["whereClauseGLCTAcctCntxt"]
      self.whereClauseGLCTEntity:str = obj["whereClauseGLCTEntity"]
      self.whereClauseGLCTJrnlCntxt:str = obj["whereClauseGLCTJrnlCntxt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGLCntrlTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLCntrlTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCntrlTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

