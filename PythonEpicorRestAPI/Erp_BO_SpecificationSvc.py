import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SpecificationSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Specifications(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Specifications items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Specifications
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications",headers=creds) as resp:
           return await resp.json()

async def post_Specifications(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Specifications
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SpecHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SpecHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Specifications_Company_SpecType_SpecID(Company, SpecType, SpecID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Specification item
   Description: Calls GetByID to retrieve the Specification item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Specification
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Specifications_Company_SpecType_SpecID(Company, SpecType, SpecID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Specification for the service
   Description: Calls UpdateExt to update Specification. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Specification
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SpecHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Specifications_Company_SpecType_SpecID(Company, SpecType, SpecID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Specification item
   Description: Call UpdateExt to delete Specification item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Specification
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Specifications_Company_SpecType_SpecID_SpecRevs(Company, SpecType, SpecID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SpecRevs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SpecRevs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")/SpecRevs",headers=creds) as resp:
           return await resp.json()

async def get_Specifications_Company_SpecType_SpecID_SpecRevs_Company_SpecType_SpecID_SpecRevNum(Company, SpecType, SpecID, SpecRevNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecRev item
   Description: Calls GetByID to retrieve the SpecRev item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecRev1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Specifications_Company_SpecType_SpecID_SpecHedAttches(Company, SpecType, SpecID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SpecHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SpecHedAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")/SpecHedAttches",headers=creds) as resp:
           return await resp.json()

async def get_Specifications_Company_SpecType_SpecID_SpecHedAttches_Company_SpecType_SpecID_DrawingSeq(Company, SpecType, SpecID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecHedAttch item
   Description: Calls GetByID to retrieve the SpecHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecHedAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/Specifications(" + Company + "," + SpecType + "," + SpecID + ")/SpecHedAttches(" + Company + "," + SpecType + "," + SpecID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecRevs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SpecRevs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SpecRevs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs",headers=creds) as resp:
           return await resp.json()

async def post_SpecRevs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SpecRevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SpecRevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SpecRevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SpecRevs_Company_SpecType_SpecID_SpecRevNum(Company, SpecType, SpecID, SpecRevNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecRev item
   Description: Calls GetByID to retrieve the SpecRev item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecRev
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SpecRevs_Company_SpecType_SpecID_SpecRevNum(Company, SpecType, SpecID, SpecRevNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SpecRev for the service
   Description: Calls UpdateExt to update SpecRev. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SpecRev
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SpecRevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SpecRevs_Company_SpecType_SpecID_SpecRevNum(Company, SpecType, SpecID, SpecRevNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SpecRev item
   Description: Call UpdateExt to delete SpecRev item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SpecRev
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecRevs_Company_SpecType_SpecID_SpecRevNum_SpecAttrs(Company, SpecType, SpecID, SpecRevNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SpecAttrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SpecAttrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")/SpecAttrs",headers=creds) as resp:
           return await resp.json()

async def get_SpecRevs_Company_SpecType_SpecID_SpecRevNum_SpecAttrs_Company_SpecType_SpecID_SpecRevNum_AttributeID(Company, SpecType, SpecID, SpecRevNum, AttributeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecAttr item
   Description: Calls GetByID to retrieve the SpecAttr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecAttr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")/SpecAttrs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecRevs_Company_SpecType_SpecID_SpecRevNum_SpecRevAttches(Company, SpecType, SpecID, SpecRevNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SpecRevAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SpecRevAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecRevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")/SpecRevAttches",headers=creds) as resp:
           return await resp.json()

async def get_SpecRevs_Company_SpecType_SpecID_SpecRevNum_SpecRevAttches_Company_SpecType_SpecID_SpecRevNum_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecRevAttch item
   Description: Calls GetByID to retrieve the SpecRevAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecRevAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecRevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + ")/SpecRevAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecAttrs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SpecAttrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SpecAttrs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs",headers=creds) as resp:
           return await resp.json()

async def post_SpecAttrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SpecAttrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SpecAttrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SpecAttrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SpecAttrs_Company_SpecType_SpecID_SpecRevNum_AttributeID(Company, SpecType, SpecID, SpecRevNum, AttributeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecAttr item
   Description: Calls GetByID to retrieve the SpecAttr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecAttr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SpecAttrs_Company_SpecType_SpecID_SpecRevNum_AttributeID(Company, SpecType, SpecID, SpecRevNum, AttributeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SpecAttr for the service
   Description: Calls UpdateExt to update SpecAttr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SpecAttr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SpecAttrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SpecAttrs_Company_SpecType_SpecID_SpecRevNum_AttributeID(Company, SpecType, SpecID, SpecRevNum, AttributeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SpecAttr item
   Description: Call UpdateExt to delete SpecAttr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SpecAttr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecAttrs_Company_SpecType_SpecID_SpecRevNum_AttributeID_SpecAttrAttches(Company, SpecType, SpecID, SpecRevNum, AttributeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SpecAttrAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SpecAttrAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecAttrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + ")/SpecAttrAttches",headers=creds) as resp:
           return await resp.json()

async def get_SpecAttrs_Company_SpecType_SpecID_SpecRevNum_AttributeID_SpecAttrAttches_Company_SpecType_SpecID_SpecRevNum_AttributeID_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, AttributeID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecAttrAttch item
   Description: Calls GetByID to retrieve the SpecAttrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecAttrAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecAttrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrs(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + ")/SpecAttrAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecAttrAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SpecAttrAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SpecAttrAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecAttrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrAttches",headers=creds) as resp:
           return await resp.json()

async def post_SpecAttrAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SpecAttrAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SpecAttrAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SpecAttrAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SpecAttrAttches_Company_SpecType_SpecID_SpecRevNum_AttributeID_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, AttributeID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecAttrAttch item
   Description: Calls GetByID to retrieve the SpecAttrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecAttrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecAttrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SpecAttrAttches_Company_SpecType_SpecID_SpecRevNum_AttributeID_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, AttributeID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SpecAttrAttch for the service
   Description: Calls UpdateExt to update SpecAttrAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SpecAttrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SpecAttrAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SpecAttrAttches_Company_SpecType_SpecID_SpecRevNum_AttributeID_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, AttributeID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SpecAttrAttch item
   Description: Call UpdateExt to delete SpecAttrAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SpecAttrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecAttrAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + AttributeID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecRevAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SpecRevAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SpecRevAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecRevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevAttches",headers=creds) as resp:
           return await resp.json()

async def post_SpecRevAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SpecRevAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SpecRevAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SpecRevAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SpecRevAttches_Company_SpecType_SpecID_SpecRevNum_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecRevAttch item
   Description: Calls GetByID to retrieve the SpecRevAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecRevAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecRevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SpecRevAttches_Company_SpecType_SpecID_SpecRevNum_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SpecRevAttch for the service
   Description: Calls UpdateExt to update SpecRevAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SpecRevAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SpecRevAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SpecRevAttches_Company_SpecType_SpecID_SpecRevNum_DrawingSeq(Company, SpecType, SpecID, SpecRevNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SpecRevAttch item
   Description: Call UpdateExt to delete SpecRevAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SpecRevAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param SpecRevNum: Desc: SpecRevNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecRevAttches(" + Company + "," + SpecType + "," + SpecID + "," + SpecRevNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SpecHedAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SpecHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SpecHedAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecHedAttches",headers=creds) as resp:
           return await resp.json()

async def post_SpecHedAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SpecHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SpecHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SpecHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecHedAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SpecHedAttches_Company_SpecType_SpecID_DrawingSeq(Company, SpecType, SpecID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SpecHedAttch item
   Description: Calls GetByID to retrieve the SpecHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SpecHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SpecHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecHedAttches(" + Company + "," + SpecType + "," + SpecID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SpecHedAttches_Company_SpecType_SpecID_DrawingSeq(Company, SpecType, SpecID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SpecHedAttch for the service
   Description: Calls UpdateExt to update SpecHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SpecHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SpecHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecHedAttches(" + Company + "," + SpecType + "," + SpecID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SpecHedAttches_Company_SpecType_SpecID_DrawingSeq(Company, SpecType, SpecID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SpecHedAttch item
   Description: Call UpdateExt to delete SpecHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SpecHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpecType: Desc: SpecType   Required: True   Allow empty value : True
      :param SpecID: Desc: SpecID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/SpecHedAttches(" + Company + "," + SpecType + "," + SpecID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SpecHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSpecHed, whereClauseSpecHedAttch, whereClauseSpecRev, whereClauseSpecRevAttch, whereClauseSpecAttr, whereClauseSpecAttrAttch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseSpecHed=" + whereClauseSpecHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSpecHedAttch=" + whereClauseSpecHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSpecRev=" + whereClauseSpecRev
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSpecRevAttch=" + whereClauseSpecRevAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSpecAttr=" + whereClauseSpecAttr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSpecAttrAttch=" + whereClauseSpecAttrAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(specType, specID, epicorHeaders = None):
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
   params += "specType=" + specType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "specID=" + specID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateRevision
   Description: To create a new SpecRev by duplicating from another.
   OperationID: DuplicateRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttributeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttributeID
   Description: Used when the Inspection Attribute field of SpecAttr is being changed to a new value.
It will validate the new AttributeID field.
   OperationID: OnChangeAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromRev
   Description: To set if duplicate option is allowed.
   OperationID: OnChangeFromRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInspPlanNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInspPlanNum
   Description: Used when the Inspection Plan Num field of SpecRev is being changed to a new value.
   OperationID: OnChangeInspPlanNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspPlanNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspPlanNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddToList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddToList
   Description: Combines value and description from RevAttrList into a delimited list
   OperationID: AddToList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SplitList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SplitList
   Description: Splits delimited list created from AddToPart into seperate value and description fields.
   OperationID: SplitList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SplitList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeListItemPosition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeListItemPosition
   Description: Moves up/down list's item one position.
   OperationID: ChangeListItemPosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeListItemPosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeListItemPosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSpecHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSpecHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSpecHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSpecHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSpecHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSpecHedAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSpecHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSpecHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSpecHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSpecHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSpecRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSpecRev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSpecRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSpecRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSpecRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSpecRevAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSpecRevAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSpecRevAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSpecRevAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSpecRevAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSpecAttr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSpecAttr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSpecAttr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSpecAttr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSpecAttr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSpecAttrAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSpecAttrAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSpecAttrAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSpecAttrAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSpecAttrAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SpecificationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecAttrAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecAttrAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecAttrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecAttrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecHedAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecHedAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecRevAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecRevAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SpecRevRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SpecRevRow] = obj["value"]
      pass

class Erp_Tablesets_SpecAttrAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SpecType:str = obj["SpecType"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.AttributeID:str = obj["AttributeID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecAttrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Revision number which is used to uniquely identify the revision of the specification, and is used as part of the primary key  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Inspection attribute key.  The value must exist in the Inspection Attribute master table (InspAttr) and must be unique to the specification detail.  """  
      self.Description:str = obj["Description"]
      """  The description of the specification detail  """  
      self.ScreenLabel:str = obj["ScreenLabel"]
      """  The label that will be shown on the Configurator input screen during the Inspection Results Entry process  """  
      self.MinDec:int = obj["MinDec"]
      """  The user defined minimum acceptable value when linked to a numeric input.  """  
      self.MaxDec:int = obj["MaxDec"]
      """  The user defined maximum acceptable value when linked to a numeric input.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used to record an inxpection value when linked to a numeric input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.InitVal:str = obj["InitVal"]
      """  The user defined value to be shown as the initial value when entering data during the inspection results entry process.  This value will be converted to the correct data type depending on the type of input the attribute is linked  """  
      self.ToolTip:str = obj["ToolTip"]
      """  The popup help message that appears when the cursor is over a control during the inspection results entry process  """  
      self.ListValues:str = obj["ListValues"]
      """  Comma delimited list of valid values that will be populated in combo box and radio set type inputs during the inspection results entry process  """  
      self.GlobalSpecAttr:bool = obj["GlobalSpecAttr"]
      """  Marks this SpecAttr as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.CmbPassValues:str = obj["CmbPassValues"]
      """  CmbPassValues  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableFields:str = obj["EnableFields"]
      self.InitDate:str = obj["InitDate"]
      self.InitDec:int = obj["InitDec"]
      self.AttrType:str = obj["AttrType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SpecType:str = obj["SpecType"]
      self.SpecID:str = obj["SpecID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.Description:str = obj["Description"]
      """  The description of the specification  """  
      self.InActive:bool = obj["InActive"]
      """  Set to true if the specification is inactive  """  
      self.GlobalSpecHed:bool = obj["GlobalSpecHed"]
      """  Marks this SpecHed as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.Description:str = obj["Description"]
      """  The description of the specification  """  
      self.InActive:bool = obj["InActive"]
      """  Set to true if the specification is inactive  """  
      self.GlobalSpecHed:bool = obj["GlobalSpecHed"]
      """  Marks this SpecHed as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecRevAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SpecType:str = obj["SpecType"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Revision number which is used to uniquely identify the revision of the specification, and is used as part of the primary key  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Revision description  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control what revision will be defaulted in applications  """  
      self.GlobalSpecRev:bool = obj["GlobalSpecRev"]
      """  Marks this SpecRev as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddToList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RevAttrListTableset] = obj["ds"]
      pass

class AddToList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listValueString:str = obj["parameters"]
      self.passValueString:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeListItemPosition_input:
   """ Required : 
   ds
   rowId
   moveType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RevAttrListTableset] = obj["ds"]
      self.rowId:str = obj["rowId"]
      self.moveType:str = obj["moveType"]
      pass

class ChangeListItemPosition_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevAttrListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RevAttrListTableset] = obj["ds"]
      self.allowMove:bool = obj["allowMove"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   specType
   specID
   """  
   def __init__(self, obj):
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateRevision_input:
   """ Required : 
   sourceSpecID
   sourceRevNum
   targetRevNum
   """  
   def __init__(self, obj):
      self.sourceSpecID:str = obj["sourceSpecID"]
      """  Existing Specification ID that will be duplicated.  """  
      self.sourceRevNum:str = obj["sourceRevNum"]
      """  Existing Revision number that will be duplicated.  """  
      self.targetRevNum:str = obj["targetRevNum"]
      """  New Revision number that will be duplicated.  """  
      pass

class DuplicateRevision_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SpecificationTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_RevAttrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  The description of List Values  """  
      self.RowType:str = obj["RowType"]
      """   If RowType is Pass it goes to the Pass List Values
If RowType is List it goes to the List Values  """  
      self.Value:str = obj["Value"]
      """  Value from the List Values or Pass List Values  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevAttrListTableset:
   def __init__(self, obj):
      self.RevAttrList:list[Erp_Tablesets_RevAttrListRow] = obj["RevAttrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SpecAttrAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SpecType:str = obj["SpecType"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.AttributeID:str = obj["AttributeID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecAttrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Revision number which is used to uniquely identify the revision of the specification, and is used as part of the primary key  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Inspection attribute key.  The value must exist in the Inspection Attribute master table (InspAttr) and must be unique to the specification detail.  """  
      self.Description:str = obj["Description"]
      """  The description of the specification detail  """  
      self.ScreenLabel:str = obj["ScreenLabel"]
      """  The label that will be shown on the Configurator input screen during the Inspection Results Entry process  """  
      self.MinDec:int = obj["MinDec"]
      """  The user defined minimum acceptable value when linked to a numeric input.  """  
      self.MaxDec:int = obj["MaxDec"]
      """  The user defined maximum acceptable value when linked to a numeric input.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used to record an inxpection value when linked to a numeric input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.InitVal:str = obj["InitVal"]
      """  The user defined value to be shown as the initial value when entering data during the inspection results entry process.  This value will be converted to the correct data type depending on the type of input the attribute is linked  """  
      self.ToolTip:str = obj["ToolTip"]
      """  The popup help message that appears when the cursor is over a control during the inspection results entry process  """  
      self.ListValues:str = obj["ListValues"]
      """  Comma delimited list of valid values that will be populated in combo box and radio set type inputs during the inspection results entry process  """  
      self.GlobalSpecAttr:bool = obj["GlobalSpecAttr"]
      """  Marks this SpecAttr as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.CmbPassValues:str = obj["CmbPassValues"]
      """  CmbPassValues  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableFields:str = obj["EnableFields"]
      self.InitDate:str = obj["InitDate"]
      self.InitDec:int = obj["InitDec"]
      self.AttrType:str = obj["AttrType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SpecType:str = obj["SpecType"]
      self.SpecID:str = obj["SpecID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.Description:str = obj["Description"]
      """  The description of the specification  """  
      self.InActive:bool = obj["InActive"]
      """  Set to true if the specification is inactive  """  
      self.GlobalSpecHed:bool = obj["GlobalSpecHed"]
      """  Marks this SpecHed as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecHedListTableset:
   def __init__(self, obj):
      self.SpecHedList:list[Erp_Tablesets_SpecHedListRow] = obj["SpecHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SpecHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.Description:str = obj["Description"]
      """  The description of the specification  """  
      self.InActive:bool = obj["InActive"]
      """  Set to true if the specification is inactive  """  
      self.GlobalSpecHed:bool = obj["GlobalSpecHed"]
      """  Marks this SpecHed as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecRevAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SpecType:str = obj["SpecType"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SpecType:str = obj["SpecType"]
      """  Specification type - Inspection, Supplier Audit, or Survey  """  
      self.SpecID:str = obj["SpecID"]
      """  User defined specificaiton code.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Revision number which is used to uniquely identify the revision of the specification, and is used as part of the primary key  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Revision description  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control what revision will be defaulted in applications  """  
      self.GlobalSpecRev:bool = obj["GlobalSpecRev"]
      """  Marks this SpecRev as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SpecificationTableset:
   def __init__(self, obj):
      self.SpecHed:list[Erp_Tablesets_SpecHedRow] = obj["SpecHed"]
      self.SpecHedAttch:list[Erp_Tablesets_SpecHedAttchRow] = obj["SpecHedAttch"]
      self.SpecRev:list[Erp_Tablesets_SpecRevRow] = obj["SpecRev"]
      self.SpecRevAttch:list[Erp_Tablesets_SpecRevAttchRow] = obj["SpecRevAttch"]
      self.SpecAttr:list[Erp_Tablesets_SpecAttrRow] = obj["SpecAttr"]
      self.SpecAttrAttch:list[Erp_Tablesets_SpecAttrAttchRow] = obj["SpecAttrAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSpecificationTableset:
   def __init__(self, obj):
      self.SpecHed:list[Erp_Tablesets_SpecHedRow] = obj["SpecHed"]
      self.SpecHedAttch:list[Erp_Tablesets_SpecHedAttchRow] = obj["SpecHedAttch"]
      self.SpecRev:list[Erp_Tablesets_SpecRevRow] = obj["SpecRev"]
      self.SpecRevAttch:list[Erp_Tablesets_SpecRevAttchRow] = obj["SpecRevAttch"]
      self.SpecAttr:list[Erp_Tablesets_SpecAttrRow] = obj["SpecAttr"]
      self.SpecAttrAttch:list[Erp_Tablesets_SpecAttrAttchRow] = obj["SpecAttrAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   specType
   specID
   """  
   def __init__(self, obj):
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SpecificationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SpecificationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SpecificationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SpecHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSpecAttrAttch_input:
   """ Required : 
   ds
   specType
   specID
   specRevNum
   attributeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      self.specRevNum:str = obj["specRevNum"]
      self.attributeID:str = obj["attributeID"]
      pass

class GetNewSpecAttrAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSpecAttr_input:
   """ Required : 
   ds
   specType
   specID
   specRevNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      self.specRevNum:str = obj["specRevNum"]
      pass

class GetNewSpecAttr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSpecHedAttch_input:
   """ Required : 
   ds
   specType
   specID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      pass

class GetNewSpecHedAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSpecHed_input:
   """ Required : 
   ds
   specType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      self.specType:str = obj["specType"]
      pass

class GetNewSpecHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSpecRevAttch_input:
   """ Required : 
   ds
   specType
   specID
   specRevNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      self.specRevNum:str = obj["specRevNum"]
      pass

class GetNewSpecRevAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSpecRev_input:
   """ Required : 
   ds
   specType
   specID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      self.specType:str = obj["specType"]
      self.specID:str = obj["specID"]
      pass

class GetNewSpecRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSpecHed
   whereClauseSpecHedAttch
   whereClauseSpecRev
   whereClauseSpecRevAttch
   whereClauseSpecAttr
   whereClauseSpecAttrAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSpecHed:str = obj["whereClauseSpecHed"]
      self.whereClauseSpecHedAttch:str = obj["whereClauseSpecHedAttch"]
      self.whereClauseSpecRev:str = obj["whereClauseSpecRev"]
      self.whereClauseSpecRevAttch:str = obj["whereClauseSpecRevAttch"]
      self.whereClauseSpecAttr:str = obj["whereClauseSpecAttr"]
      self.whereClauseSpecAttrAttch:str = obj["whereClauseSpecAttrAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SpecificationTableset] = obj["returnObj"]
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

class OnChangeAttributeID_input:
   """ Required : 
   newAttributeID
   ds
   """  
   def __init__(self, obj):
      self.newAttributeID:str = obj["newAttributeID"]
      """  The new Attribute ID value.  """  
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

class OnChangeAttributeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromRev_input:
   """ Required : 
   sourceSpecID
   sourceRevNum
   """  
   def __init__(self, obj):
      self.sourceSpecID:str = obj["sourceSpecID"]
      """  Existing Specification that will be duplicated.  """  
      self.sourceRevNum:str = obj["sourceRevNum"]
      """  Existing Revision number that will be duplicated.  """  
      pass

class OnChangeFromRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oKToDuplicate:bool = obj["oKToDuplicate"]
      pass

      """  output parameters  """  

class OnChangeInspPlanNum_input:
   """ Required : 
   newInspPlan
   ds
   """  
   def __init__(self, obj):
      self.newInspPlan:str = obj["newInspPlan"]
      """  The Insp plan value.  """  
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

class OnChangeInspPlanNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SplitList_input:
   """ Required : 
   listValue
   passListValue
   """  
   def __init__(self, obj):
      self.listValue:str = obj["listValue"]
      """  Delimited list from SpecAttr.ListValues.  """  
      self.passListValue:str = obj["passListValue"]
      """  Delimited list from SpecAttr.CmbPassValues.  """  
      pass

class SplitList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevAttrListTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSpecificationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSpecificationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SpecificationTableset] = obj["ds"]
      pass

      """  output parameters  """  

