import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ImageSvc
# Description: ImageSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Images(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Images items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Images
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/Images",headers=creds) as resp:
           return await resp.json()

async def post_Images(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Images
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ImageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/Images", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Images_Company_ImageID(Company, ImageID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Image item
   Description: Calls GetByID to retrieve the Image item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Image
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageID: Desc: ImageID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/Images(" + Company + "," + ImageID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Images_Company_ImageID(Company, ImageID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Image for the service
   Description: Calls UpdateExt to update Image. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Image
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageID: Desc: ImageID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/Images(" + Company + "," + ImageID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Images_Company_ImageID(Company, ImageID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Image item
   Description: Call UpdateExt to delete Image item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Image
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageID: Desc: ImageID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/Images(" + Company + "," + ImageID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImageListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseImage, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseImage=" + whereClauseImage
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(imageID, epicorHeaders = None):
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
   params += "imageID=" + imageID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultsFromCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultsFromCompany
   OperationID: GetDefaultsFromCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultsFromCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsFromCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOriginalImageWithFileType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOriginalImageWithFileType
   Description: Returns the image data along with the file type for an image ID
   OperationID: GetOriginalImageWithFileType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOriginalImageWithFileType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOriginalImageWithFileType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOriginalImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOriginalImage
   Description: Returns the image data for an image ID
   OperationID: GetOriginalImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOriginalImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOriginalImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsImageID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsImageID
   OperationID: ExistsImageID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsImageID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsImageID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckImageCategoryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckImageCategoryID
   OperationID: CheckImageCategoryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckImageCategoryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckImageCategoryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckImageSubCategoryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckImageSubCategoryID
   OperationID: CheckImageSubCategoryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckImageSubCategoryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckImageSubCategoryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportStyleImages
   Description: Exports the report style images. This is used by Solution Workbench to export images for a report.
   OperationID: ExportReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportStyleImages
   Description: Imports the report style images.
   OperationID: ImportReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportImages
   OperationID: ImportImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportMutipleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportMutipleImages
   OperationID: ImportMutipleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportMutipleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportMutipleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadLocalImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadLocalImage
   OperationID: UploadLocalImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadLocalImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadLocalImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ColumnChangingImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ColumnChangingImages
   Description: Get ImageID
   OperationID: ColumnChangingImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColumnChangingImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnChangingImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCategoryFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCategoryFile
   Description: verify format of importCategoryFile
   OperationID: ValidateCategoryFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCategoryFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCategoryFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyImportCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyImportCategory
   OperationID: VerifyImportCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyImportCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyImportCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForImage
   Description: Gets the list of Images for the session company and Global Images.
   OperationID: GetRowsForImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImageListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImageListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImageRow] = obj["value"]
      pass

class Erp_Tablesets_ImageListRow:
   def __init__(self, obj):
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ImageCategoryID:str = obj["ImageCategoryID"]
      """  ImageCategoryID  """  
      self.ImageSubCategoryID:str = obj["ImageSubCategoryID"]
      """  ImageSubCategoryID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  ModifiedBy  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  ImageFileName  """  
      self.ImageFileThumbnail:str = obj["ImageFileThumbnail"]
      """  ImageFileThumbnail  """  
      self.ImageCategoryID:str = obj["ImageCategoryID"]
      """  ImageCategoryID  """  
      self.ImageSubCategoryID:str = obj["ImageSubCategoryID"]
      """  ImageSubCategoryID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  ModifiedBy  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.FileSize:int = obj["FileSize"]
      """  FileSize  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.GlobalImage:bool = obj["GlobalImage"]
      """  GlobalImage  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Reference1:str = obj["Reference1"]
      """  Reference1  """  
      self.Reference2:str = obj["Reference2"]
      """  Reference2  """  
      self.Reference3:str = obj["Reference3"]
      """  Reference3  """  
      self.Reference4:str = obj["Reference4"]
      """  Reference4  """  
      self.Reference5:str = obj["Reference5"]
      """  Reference5  """  
      self.ThumbnailSysRowID:str = obj["ThumbnailSysRowID"]
      """  ThumbnailSysRowID  """  
      self.ImageSysRowID:str = obj["ImageSysRowID"]
      """  ImageSysRowID  """  
      self.ImageCategoryDesc:str = obj["ImageCategoryDesc"]
      self.ImageContent:str = obj["ImageContent"]
      self.ImageSubCategoryDesc:str = obj["ImageSubCategoryDesc"]
      self.ThumbnailContent:str = obj["ThumbnailContent"]
      self.LocalImageFile:str = obj["LocalImageFile"]
      """  Local Image File  """  
      self.ServerImageFile:str = obj["ServerImageFile"]
      """  Server Image File  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckImageCategoryID_input:
   """ Required : 
   categoryID
   ds
   """  
   def __init__(self, obj):
      self.categoryID:str = obj["categoryID"]
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

class CheckImageCategoryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckImageSubCategoryID_input:
   """ Required : 
   categoryID
   subcategoryID
   ds
   """  
   def __init__(self, obj):
      self.categoryID:str = obj["categoryID"]
      self.subcategoryID:str = obj["subcategoryID"]
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

class CheckImageSubCategoryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ColumnChangingImages_input:
   """ Required : 
   importFileName
   removeExt
   """  
   def __init__(self, obj):
      self.importFileName:str = obj["importFileName"]
      self.removeExt:bool = obj["removeExt"]
      pass

class ColumnChangingImages_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   imageID
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ImageListRow:
   def __init__(self, obj):
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ImageCategoryID:str = obj["ImageCategoryID"]
      """  ImageCategoryID  """  
      self.ImageSubCategoryID:str = obj["ImageSubCategoryID"]
      """  ImageSubCategoryID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  ModifiedBy  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageListTableset:
   def __init__(self, obj):
      self.ImageList:list[Erp_Tablesets_ImageListRow] = obj["ImageList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  ImageFileName  """  
      self.ImageFileThumbnail:str = obj["ImageFileThumbnail"]
      """  ImageFileThumbnail  """  
      self.ImageCategoryID:str = obj["ImageCategoryID"]
      """  ImageCategoryID  """  
      self.ImageSubCategoryID:str = obj["ImageSubCategoryID"]
      """  ImageSubCategoryID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedBy:str = obj["ModifiedBy"]
      """  ModifiedBy  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.FileSize:int = obj["FileSize"]
      """  FileSize  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.GlobalImage:bool = obj["GlobalImage"]
      """  GlobalImage  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Reference1:str = obj["Reference1"]
      """  Reference1  """  
      self.Reference2:str = obj["Reference2"]
      """  Reference2  """  
      self.Reference3:str = obj["Reference3"]
      """  Reference3  """  
      self.Reference4:str = obj["Reference4"]
      """  Reference4  """  
      self.Reference5:str = obj["Reference5"]
      """  Reference5  """  
      self.ThumbnailSysRowID:str = obj["ThumbnailSysRowID"]
      """  ThumbnailSysRowID  """  
      self.ImageSysRowID:str = obj["ImageSysRowID"]
      """  ImageSysRowID  """  
      self.ImageCategoryDesc:str = obj["ImageCategoryDesc"]
      self.ImageContent:str = obj["ImageContent"]
      self.ImageSubCategoryDesc:str = obj["ImageSubCategoryDesc"]
      self.ThumbnailContent:str = obj["ThumbnailContent"]
      self.LocalImageFile:str = obj["LocalImageFile"]
      """  Local Image File  """  
      self.ServerImageFile:str = obj["ServerImageFile"]
      """  Server Image File  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageTableset:
   def __init__(self, obj):
      self.Image:list[Erp_Tablesets_ImageRow] = obj["Image"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtImageTableset:
   def __init__(self, obj):
      self.Image:list[Erp_Tablesets_ImageRow] = obj["Image"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsImageID_input:
   """ Required : 
   imageID
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      pass

class ExistsImageID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExportReportStyleImages_input:
   """ Required : 
   reportId
   styleNumber
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.styleNumber:int = obj["styleNumber"]
      """  The style number.  """  
      pass

class ExportReportStyleImages_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The image information for the specified report style.  """  
      pass

class GetByID_input:
   """ Required : 
   imageID
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImageTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImageTableset] = obj["returnObj"]
      pass

class GetDefaultsFromCompany_input:
   """ Required : 
   applicationName
   """  
   def __init__(self, obj):
      self.applicationName:str = obj["applicationName"]
      pass

class GetDefaultsFromCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.category:str = obj["parameters"]
      self.subCategory:str = obj["parameters"]
      self.categoryDesc:str = obj["parameters"]
      self.SubcategoryDesc:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_ImageListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewImage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

class GetNewImage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOriginalImageWithFileType_input:
   """ Required : 
   imageID
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      pass

class GetOriginalImageWithFileType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.fileType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetOriginalImage_input:
   """ Required : 
   imageID
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      pass

class GetOriginalImage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRowsForImage_input:
   """ Required : 
   whereClause
   startingAt
   hDCaseNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.startingAt:str = obj["startingAt"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.hDCaseNum:int = obj["hDCaseNum"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetRowsForImage_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseImage
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseImage:str = obj["whereClauseImage"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageTableset] = obj["returnObj"]
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

class ImportImages_input:
   """ Required : 
   imageID
   fileNames
   images
   imgWidth
   imgHeight
   imgSize
   imgType
   removeExtensions
   renameDuplicates
   updateDuplicates
   categoryID
   subcategoryID
   importCategories
   importCategoryInfo
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      self.fileNames:str = obj["fileNames"]
      self.images:str = obj["images"]
      self.imgWidth:int = obj["imgWidth"]
      self.imgHeight:int = obj["imgHeight"]
      self.imgSize:int = obj["imgSize"]
      self.imgType:str = obj["imgType"]
      self.removeExtensions:bool = obj["removeExtensions"]
      self.renameDuplicates:bool = obj["renameDuplicates"]
      self.updateDuplicates:bool = obj["updateDuplicates"]
      self.categoryID:str = obj["categoryID"]
      self.subcategoryID:str = obj["subcategoryID"]
      self.importCategories:str = obj["importCategories"]
      self.importCategoryInfo:bool = obj["importCategoryInfo"]
      pass

class ImportImages_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.imageImported:list = obj[any]
      pass

      """  output parameters  """  

class ImportMutipleImages_input:
   """ Required : 
   method
   imageID
   imageFileServer
   multipeImagesServer
   removeExtensions
   renameDuplicates
   updateDuplicates
   categoryID
   subcategoryID
   importCategoryInfo
   importCategoryServerFile
   """  
   def __init__(self, obj):
      self.method:str = obj["method"]
      self.imageID:str = obj["imageID"]
      self.imageFileServer:str = obj["imageFileServer"]
      self.multipeImagesServer:str = obj["multipeImagesServer"]
      self.removeExtensions:bool = obj["removeExtensions"]
      self.renameDuplicates:bool = obj["renameDuplicates"]
      self.updateDuplicates:bool = obj["updateDuplicates"]
      self.categoryID:str = obj["categoryID"]
      self.subcategoryID:str = obj["subcategoryID"]
      self.importCategoryInfo:bool = obj["importCategoryInfo"]
      self.importCategoryServerFile:str = obj["importCategoryServerFile"]
      pass

class ImportMutipleImages_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.imageImported:list = obj[any]
      pass

      """  output parameters  """  

class ImportReportStyleImages_input:
   """ Required : 
   exportDataSet
   """  
   def __init__(self, obj):
      self.exportDataSet      #schema had no properties on an object.
      """  The export data set.  """  
      pass

class ImportReportStyleImages_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImageTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImageTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadLocalImage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

class UploadLocalImage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCategoryFile_input:
   """ Required : 
   importCategoryFile
   importCategoryInfo
   """  
   def __init__(self, obj):
      self.importCategoryFile:str = obj["importCategoryFile"]
      self.importCategoryInfo:bool = obj["importCategoryInfo"]
      pass

class ValidateCategoryFile_output:
   def __init__(self, obj):
      pass

class VerifyImportCategory_input:
   """ Required : 
   categoryID
   subcategoryID
   """  
   def __init__(self, obj):
      self.categoryID:str = obj["categoryID"]
      self.subcategoryID:str = obj["subcategoryID"]
      pass

class VerifyImportCategory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.categoryIDDesc:str = obj["parameters"]
      self.subcategoryIDDesc:str = obj["parameters"]
      self.subcategoryIDUpdate:str = obj["parameters"]
      pass

      """  output parameters  """  

